from .models import BaseUser
from rest_framework.serializers import ModelSerializer


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model=BaseUser
        fields=['email','password']


class UserSerializer(ModelSerializer):
    class Meta:
        model=BaseUser
        fields=['id','email','first_name','last_name','phone']