from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.db.models import Q, Count

from .serializer import *
from siteconfig.functions import get_validation_error_message, method_not_allowed

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs): # Create new reivew 
        try:
        # if 1==1:
            user = request.user
            data = request.data
            data["username"] = data.get("email", None)
            data["is_staff"] = True
            if user.is_superuser:
                # serializer = UserSerializer(data=data)
                serializer = self.get_serializer(data=data)
                if serializer.is_valid():
                    serializer.save()

                    user_data = User.objects.filter(email__iexact=data["email"]).first()
                    user_data.set_password(data["password"])
                    user_data.save()

                    return Response({"status" : "success", "data": serializer.data, "error": {"error_message":"User created successfully.","error_code":"success"}, "extra_data" : {}},status=200)
                else:
                    error_message = get_validation_error_message(serializer)
                    return Response({"status" : "failure", "data":{}, "error": {"error_message":error_message ,"error_code":"error"}, "extra_data" : {}}, status=400)
            else:
                return Response({"status" : "failure", "data": {}, "error": {"error_message":"Access Aenied","error_code":"access_denied"}, "extra_data" : {}}, status=400)      
        except ValidationError as ve:
            return Response({"status" : "failure", "data": {}, "error": {"error_message":ve.messages[0],"error_code":"error"}, "extra_data" : {}}, status=400)            
        except Exception as e:
            print("exception - ",e) 
            return Response({"status" : "failure", "data": {}, "error": {"error_message":"Something went wrong", "error_code":"error"}, "extra_data" : {}}, status=400)  
        

    def list(self, request):
        try:
        # if 1==1:
            all_users = User.objects.filter(~Q(email__iexact = request.user.email), is_active=True)
            print(all_users)
            serialized_data = UserSerializer(all_users, many=True).data
            if serialized_data:
                return Response({"status" : "success", "data": serialized_data, "error": {"error_message":" Success ","error_code":"success"}, "extra_data" : {}},status=200)
            else:
                return Response({"status" : "failure", "data": [], "error": {"error_message":"Users not found.","error_code":"error"}, "extra_data" : {}},status=404)
        except ValidationError as ve:
            return Response({"status" : "failure", "data": {}, "error": {"error_message":ve.messages[0],"error_code":"error"}, "extra_data" : {}}, status=400)            
        except Exception as e:
            print("exception - ",e) 
            return Response({"status" : "failure", "data": {}, "error": {"error_message":"Something went wrong", "error_code":"error"}, "extra_data" : {}}, status=400)  
        
    

class LoginView(APIView):

    def post(self, request):
        # check if  Internal-Call-Token is valid 
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                print("user all attribute -----", user.__dict__)
                token, created = Token.objects.get_or_create(user=user)
                # print(token)
                data = {
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email,
                    'username':user.username,
                    'is_superuser':user.is_superuser,

                }
                return Response({"status" : "success", "data": data, "error": {"error_message":"success","error_code":"error"}, "extra_data" : {}},status=400)
            else:
                
                return Response({"status" : "failure", "data": {}, "error": {"error_message":"error","error_code":"success"}, "extra_data" : {}},status=200)
        except Exception as e:
            print(e)
            return Response({"status" : "failure", "data": {}, "error": {"error_message":"Something went wrong","error_code":"error"}, "extra_data" : {}},status=400)
