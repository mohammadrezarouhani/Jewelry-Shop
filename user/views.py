from django.contrib.auth.password_validation import validate_password
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BaseUser
from .serializer import UserRegisterSerializer, UserSerializer,PasswordSerializer
from rest_framework.permissions import IsAuthenticated

class UserRegister(generics.CreateAPIView):
    queryset=BaseUser.objects.all()
    serializer_class=UserRegisterSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=BaseUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]


class PasswordReset(generics.UpdateAPIView):
    serializer_class=PasswordSerializer
    model=BaseUser
    permission_classes=[IsAuthenticated]
  
    def get_object(self):
        try:
            return BaseUser.objects.get(pk=self.kwargs['pk'])
        except:
            return Response(status.HTTP_404_NOT_FOUND)


    def update(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        user=self.get_object()

        if serializer.is_valid():

            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old password':'password is wrong!!!'},status=status.HTTP_204_NO_CONTENT)
            else:
                try:
                    validate_password(serializer.data.get('new_password'))
                except Exception as ex:
                    return Response({'password':ex},status=status.HTTP_406_NOT_ACCEPTABLE)

                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response({'new password':'password changed'},status=status.HTTP_200_OK) 

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)