from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff', 'is_superuser', 'is_active']
        extra_kwargs = {
                        'password': {'write_only': True},
                       }
        read_only_fields = ['is_superuser']
