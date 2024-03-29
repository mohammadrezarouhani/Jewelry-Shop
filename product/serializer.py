from ast import Delete
from rest_framework import serializers
from .models import Factor, Product, FactorProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class ProductSoldSerializer(serializers.ModelSerializer):
    class Meta:
        model=FactorProduct
        fields=['id','product','name','price','tax','discount','date_added','number']


class FactorSerializer(serializers.ModelSerializer):
    product_sold=ProductSoldSerializer(many=True)
    total_price=serializers.SerializerMethodField(method_name='get_total_price')
    
    class Meta:
        model=Factor
        fields=['id','seller','customer_name',
                'payment_type','comment','date',"product_sold"]
    
    def get_total_price(self,product):
        return product.prefetch_related('product_sold')     #TODO   should exec some query to db for getting 
    
    def create(self, validated_data):
        product=validated_data.pop('product_sold')
        factor=Factor.objects.create(**validated_data)

        for data in product:
            FactorProduct.objects.create(**data,factor=factor)
        return factor
    
    def update(self, instance, validated_data):
        product=validated_data.pop("product_sold")
        FactorProduct.objects.filter(factor=instance).delete()

        for data in product:
            FactorProduct.objects.create(**data,factor=instance)

        return super().update(instance,validated_data)


class DailyPriceSerializer(serializers.Serializer):
    daily_sale=serializers.CharField(max_length=255)
    date=serializers.DateField()


class MonthlyPriceSerializer(serializers.Serializer):
    daily_sale=serializers.CharField(max_length=255)
    date__month=serializers.CharField(max_length=25)
    date__year=serializers.CharField(max_length=25)