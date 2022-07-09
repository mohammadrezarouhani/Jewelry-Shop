import email
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.hashers import make_password
from user.models import BaseUser


class UserTest(APITestCase):
    def setUp(self):
        password = make_password('pass')
        self.user = BaseUser.objects.create(
            username='test', email='test@test.com', password=password)

        url = reverse('token-obtain')
        resp = self.client.post(url, data=dict(
            email='test@test.com', password='pass'), format='json')
        self.refresh_token = resp.data.get('refresh')
        self.access_token = resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(self.access_token))
        return super().setUp()


    def test_user_register(self):
        url = reverse('user-register')
        data = dict(username='test1', email='test1@test.com', password='test')
        resp = self.client.post(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


    def test_user_detail(self):
        user = {
                'username': 'new',
                'email': 'new@test.com',
                'password': 'pass'
                }
        user=BaseUser.objects.create(**user)
        url_detail = reverse('user-detail', kwargs={'pk': user.pk})
        resp = self.client.get(url_detail)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        edited_user = {
                    "id":user.pk,
                    "username": "new",
                    "email": "new@test.com",
                    "first_name": "test",
                    "last_name": "test",
                    "phone": "+9142456325"
                    }
        resp = self.client.put(url_detail, data=edited_user, format='json')
        self.assertEqual(resp.status_code,status.HTTP_200_OK)

        resp=self.client.delete(url_detail)
        self.assertEqual(resp.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(resp.data,None)


    def test_password_reset(self):
        url = reverse('password-reset', kwargs={'pk': '1'})
        data = dict(old_password='pass', new_password='new_password')
        resp = self.client.put(url, data=data, format='json')
        self.assertEqual(resp.status_code,status.HTTP_200_OK)


    def test_jwt_token(self):
        url = reverse('token-obtain')
        resp = self.client.post(url, data=dict(
            email='test@test.com', password='pass'), format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data and 'refresh' in resp.data)