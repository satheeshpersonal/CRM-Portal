from rest_framework import serializers
from .models import *


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        exclude = ['created','updated']
        extra_kwargs = {
                        'updated_by': {'write_only': True},
                        'created': {'write_only': True},
                        'updated': {'write_only': True},
                       }
        
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        exclude = ['created','updated']
        extra_kwargs = {
                        'updated_by': {'write_only': True},
                        'created': {'write_only': True},
                        'updated': {'write_only': True},
                       }

class ClientAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientAccess
        exclude = ['created','updated']
        extra_kwargs = {
                        'created': {'write_only': True},
                        'updated': {'write_only': True},
                       }