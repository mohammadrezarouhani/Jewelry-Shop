from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class BaseUser(AbstractUser):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    first_name=models.CharField(max_length=55,blank=True,null=True)
    last_name=models.CharField(max_length=55,blank=True,null=True)
    username=models.CharField(max_length=75,unique=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=55,blank=True,null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']


    def __str__(self) -> str:
        return "{} ({})".format(self.email,self.id)