from pyexpat import model
from .models import BaseUser
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=BaseUser
        fields=['email','password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=BaseUser
        fields=['id','username','email','first_name','last_name','phone']


class PasswordSerializer(serializers.Serializer):
    model=BaseUser
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)