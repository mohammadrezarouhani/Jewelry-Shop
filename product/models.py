from PIL import Image
from django.db import models
from django.forms import modelformset_factory
from user.models import BaseUser
from django.utils import timezone


class Product(models.Model):
    TYPE=(['co','coin'],['jew','jewelry'],['go','gold_bullion'])
    UNIT=(['o','ons'],['m','methghal'],['gr','geram'])
    COIN='co'
    GRAM='gr'
    user=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='product_user')
    name=models.CharField(max_length=55)
    price=models.PositiveIntegerField()
    type=models.CharField(choices=TYPE,max_length=55,default=COIN)
    weight=models.FloatField(default=0.0)
    unit=models.CharField(choices=UNIT,max_length=55,default=GRAM)
    inventory=models.PositiveSmallIntegerField()
    date_added=models.DateField(auto_now=True)
    image=models.ImageField(default='def.jpg',upload_to='product_image')
    description=models.CharField(max_length=255,blank=True,null=True)

    def save(self,*args,**kwargs):
        super().save()
        img=Image.open(self.image.path)
        if img.height>500 or img.width>500:
            img.thumbnail((500,500))
            img.save(self.image.path)
        img.close()
    
    def __str__(self) -> str:
        return "{} ({})".format(self.name,self.id)


class Factor(models.Model):
    CASH='csh'
    CREDIT='crd'
    PAYMENT=(['csh','cash'],['crd','credit'])

    seller=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=155)
    payment_type = models.CharField(choices=PAYMENT,default=CASH,max_length=55)
    comment = models.CharField(max_length=755,null=True,blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name}({self.id})"
    

class FactorProduct(models.Model):
    factor=models.ForeignKey(Factor,on_delete=models.CASCADE,related_name='product_sold')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=155)
    price=models.PositiveIntegerField()
    tax=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    number=models.IntegerField()
    date_added=models.DateField(auto_now=True)

    def __str__(self) :     
        return f"{self.name}{self.id}"
