from rest_framework import generics
from .models import BaseUser
from .serializer import UserRegisterSerializer, UserSerializer


class UserRegister(generics.CreateAPIView):
    queryset=BaseUser.objects.all()
    serializer_class=UserRegisterSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=BaseUser.objects.all()
    serializer_class=UserSerializer