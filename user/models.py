from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseUser(AbstractUser):
    first_name=models.CharField(max_length=55,blank=True,null=True)
    last_name=models.CharField(max_length=55,blank=True,null=True)
    username=models.CharField(max_length=75,unique=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=55,blank=True,null=True)
    image=models.ImageField(default='def.jpg',upload_to='profile_image')
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']


    def save(self,*args, **kwargs):
        super().save()
        img=Image.open(self.image.path)
        if img.height>500 and img.width >500:
            img.thumbnail((500,500))
            img.save(self.image.path)
        img.close()
        

    def __str__(self) -> str:
        return "{} ({})".format(self.email,self.id)