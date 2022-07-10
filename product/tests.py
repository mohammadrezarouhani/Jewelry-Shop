import pdb
from rest_framework.test import APITestCase
from user.models import BaseUser
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.urls import reverse
from .models import FactorProduct, Product, Factor


class TestProduct(APITestCase):
    def create_fake_data(self):
        # user 
        password = make_password('pass')
        self.user = BaseUser.objects.create(username='test', email='test@test.com', password=password)
        # authentication
        url = reverse('token-obtain')
        resp = self.client.post(url, data=dict(email='test@test.com', password='pass'), format='json')
        token = resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(token))

        # fake data base by test user we created 
        self.product_json = {
            'user': self.user.id,
            'name': 'test',
            'type': 'jew',
            'price': 20000000000,
            'weight': 20.55,
            'unit': 'm',
            'inventory': 3,
            'description': 'test disc'
        }
        self.product_json_for_create_object = {
            'user': self.user,
            'name': 'test',
            'type': 'jew',
            'price': 20000000000,
            'weight': 20.55,
            'unit': 'm',
            'inventory': 3,
            'description': 'test disc'
        }
        self.product_object = Product.objects.create(**self.product_json_for_create_object)

        self.edited_product_json = {
            'id': self.product_object.id,
            'user': self.user.id,
            'name': 'test edited',
            'type': 'co',
            'price': 20000000000,
            'weight': 20.55,
            'unit': 'o',
            'inventory': 3,
            'description': 'test disc'
        }
        self.factor_json = {
            'seller': self.user.id,
            'customer_name': 'test',
            'payment_type': 'csh',
            'comment': 'test',
            'product_sold': [
                {
                    'name': 'test',
                    'product': self.product_object.id,
                    'number': 2,
                    'price': 100000,
                    'tax': 10000,
                    'discount': 10000
                },
            ]
        }
        self.factor_without_product_sold={
            'seller': self.user,
            'customer_name': 'test',
            'payment_type': 'csh',
            'comment': 'test'
        }
        self.factor_object = Factor.objects.create(**self.factor_without_product_sold)

        self.edited_factor_json={
            'seller': self.user.id,
            'customer_name': 'test',
            'payment_type': 'crd',
            'comment': 'test edited',
            'product_sold': [
                {
                    'name': 'test edited',
                    'product': self.product_object.id,
                    'number': 1,
                    'price': 200000,
                    'tax': 20000,
                    'discount': 20000
                },
            ]
        }
        self.product_sold_json_for_create_object = {
            'factor': self.factor_object,
            'name': 'test',
            'product': self.product_object,
            'number': 4,
            'price': '100000',
            'tax': 1000,
            'discount': 10000
        }
        
        self.product_sold_object = FactorProduct.objects.create(**self.product_sold_json_for_create_object)
        

    def setUp(self):
        self.create_fake_data()
        return super().setUp()

    def test_product_list(self):
        url = '{}?user={}'.format(reverse('product-list'), self.user.id)
        data = {
            'user': self.user.id,
            'name': 'test',
            'type': 'jew',
            'price': 20000000000,
            'weight': 20.55,
            'unit': 'm',
            'inventory': 3,
            'description': 'test disc'
        }
        resp = self.client.post(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('user' in resp.data[0])

    def test_product_detail(self):
        data = {
            'user': self.user,
            'name': 'test',
            'type': 'jew',
            'price': 20000000000,
            'weight': 20.55,
            'unit': 'm',
            'inventory': 3,
            'description': 'test disc'
        }
        product = Product.objects.create(**data)
        url = reverse('product-detail', kwargs={'pk': product.id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('test' == resp.data.get('name'))

        edited_data = {
            'id': product.id,
            'user': self.user.id,
            'name': 'test edited',
            'type': 'co',
            'price': 20000000000,
            'weight': 20.55,
            'unit': 'o',
            'inventory': 3,
            'description': 'test disc'
        }
        resp = self.client.put(url, data=edited_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('test edited' == resp.data.get('name'))

        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(resp.data == None)

    def test_factor_list(self):
        url = '{}?seller={}'.format(reverse('factor-list'), self.user.id)
        product_json = {
            'user': self.user,
            'name': 'test',
            'type': 'jew',
            'price': 20000000000,
            'weight': 20.55,
            'unit': 'm',
            'inventory': 3,
            'description': 'test disc'
        }
        product_object = Product.objects.create(**product_json)
        factor_json = {
            'seller': self.user.id,
            'customer_name': 'test',
            'payment_type': 'csh',
            'comment': 'test',
            'product_sold': [
                {
                    'name': 'test',
                    'product': product_object.id,
                    'number': 2,
                    'price': 100000,
                    'tax': 10000,
                    'discount': 10000
                },
            ]
        }
        resp = self.client.post(url, data=factor_json, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue('test' in resp.data.values())

    def test_factor_detail(self):
        # creating a product record for future use
        product_json = {
            'user': self.user,
            'name': 'test',
            'type': 'jew',
            'price': 10000,
            'weight': 20.55,
            'unit': 'm',
            'inventory': 3,
            'description': 'test disc'
        }
        product_object = Product.objects.create(**product_json)

        # creatign a factor record in db
        factor_json = {
            'seller': self.user,
            'customer_name': 'test',
            'payment_type': 'csh',
            'comment': 'test'
        }
        factor_object = Factor.objects.create(**factor_json)

        # adding a product to factor record in db
        product_sold_json = {
            'factor': factor_object,
            'name': 'test',
            'product': product_object,
            'number': 4,
            'price': '100000',
            'tax': 1000,
            'discount': 10000
        }

        FactorProduct.objects.create(**product_sold_json)

        url = reverse('factor-detail', kwargs={'pk': factor_object.id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('product_sold' in resp.data)

        edited_factor_json = {
            'seller': self.user.id,
            'customer_name': 'test',
            'payment_type': 'crd',
            'comment': 'test edited',
            'product_sold': [
                {
                    'name': 'test edited',
                    'product': product_object.id,
                    'number': 1,
                    'price': 200000,
                    'tax': 20000,
                    'discount': 20000
                },
            ]
        }
        resp = self.client.put(url, edited_factor_json, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('test edited' in resp.data.values())

    def test_daily_sale(self):
        url = reverse('daily-sale', kwargs={'user': self.user.id})

    def test_monthly_sale(self):
        url = reverse('monthly-sale', kwargs={'user': self.user.id})

    def test_currency_info(self):
        url = reverse('currency-info')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('currency' in resp.data)
