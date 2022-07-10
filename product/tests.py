import pdb
from rest_framework.test import APITestCase
from user.models import BaseUser
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.urls import reverse
from .models import FactorProduct, Product,Factor


class TestProduct(APITestCase):
    def setUp(self):
        password=make_password('pass')
        self.user=BaseUser.objects.create(username='test',email='test@test.com',password=password)

        url=reverse('token-obtain')
        resp=self.client.post(url,data=dict(email='test@test.com',password='pass'),format='json')
        token=resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(token))
        return super().setUp()


    def test_product_list(self):
        url='{}?user={}'.format(reverse('product-list'),self.user.id)
        data={
            'user':self.user.id,
            'name':'test',
            'type':'jew',
            'price':20000000000,
            'weight':20.55,
            'unit':'m',
            'inventory':3,
            'description':'test disc'
        }
        resp=self.client.post(url,data=data,format='json')
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)

        resp=self.client.get(url)
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        self.assertTrue('user' in resp.data[0])


    def test_product_detail(self):
        data={
            'user':self.user,
            'name':'test',
            'type':'jew',
            'weight':20.55,
            'unit':'m',
            'inventory':3,
            'description':'test disc'
        }
        product=Product.objects.create(**data)
        url=reverse('product-detail',kwargs={'pk':product.id})
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        self.assertTrue('test' == resp.data.get('name'))

        edited_data={
            'id':product.id,
            'user':self.user.id,
            'name':'test edited',
            'type':'co',
            'weight':20.55,
            'unit':'o',
            'inventory':3,
            'description':'test disc'
        }
        resp=self.client.put(url,data=edited_data,format='json')
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        self.assertTrue('test edited' == resp.data.get('name'))

        resp=self.client.delete(url)
        self.assertEqual(resp.status_code,status.HTTP_204_NO_CONTENT)
        self.assertTrue(resp.data == None)


    def test_factor_list(self):
        url='{}?seller={}'.format(reverse('factor-list'),self.user.id)
        data={
            'user':self.user,
            'name':'test',
            'type':'jew',
            'weight':20.55,
            'unit':'m',
            'inventory':3,
            'description':'test disc'
        }
        product=Product.objects.create(**data)
        data={
            'seller':self.user.id,
            'customer_name':'test',
            'payment_type':'csh',
            'total_price':'500000',
            'tax':100000,
            'discount':10000,
            'comment':'test',
            'product_sold':[
                {
                    'name':'test',
                    'product':product.id,
                    'number':4,
                    'price':'100000',
                },
            ]
        }
        resp=self.client.post(url,data=data,format='json')
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)
        self.assertTrue('product_sold' in resp.data)


    def test_factor_detail(self):
        # creating a product record for future use
        data={
            'user':self.user,
            'name':'test',
            'type':'jew',
            'weight':20.55,
            'unit':'m',
            'inventory':3,
            'description':'test disc'
        }
        product=Product.objects.create(**data)
        
        # creatign a factor record in db
        data={
            'seller':self.user,
            'customer_name':'test',
            'payment_type':'csh',
            'total_price':'500000',
            'tax':100000,
            'discount':10000,
            'comment':'test'
        }
        factor=Factor.objects.create(**data)

        # adding a product to factor record in db
        data={
            'factor':factor,
            'name':'test',
            'product':product,
            'number':4,
            'price':'100000',
        }
        product_sold=FactorProduct.objects.create(**data)

        url=reverse('factor-detail',kwargs={'pk':factor.id})
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        self.assertTrue('product_sold' in resp.data)
        

    def test_daily_sale(self):
        url=reverse('daily-sale',kwargs={'user':self.user.id})

    def test_monthly_sale(self):
        url=reverse('monthly-sale',kwargs={'user':self.user.id})


    def test_currency_info(self):
        url=reverse('currency-info')
        resp=self.client.get(url)        
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        self.assertTrue('currency' in resp.data)