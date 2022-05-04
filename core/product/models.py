from tkinter import Image
from django.db import models
import uuid
from django.utils import timezone
from user.models import BaseUser

TYPE=(['coin',1],['jewelry',2],['gold_bullion',3])
UNIT=(['ons',1],['methghal',2],['geram',3])

class Product(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    user=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='product_user')
    name=models.CharField(max_length=55)
    type=models.CharField(max_length=55,choices=TYPE)
    weight=models.FloatField(default=0.0)
    unit=models.CharField(max_length=15,choices=UNIT)
    date=models.DateField(timezone.now)
    image=models.ImageField(default='def.jpg',upload_to='product_image')
    description=models.CharField(max_length=255,blank=True,null=True)

    def save(self):
        super().save()
        img=Image(self.image.path)
        if img.height>100 or img.width>100:
            img.thumbnail((100,100))
            img.save()
    
    def __str__(self) -> str:
        return "{} ()".format(self.name,self.id)

