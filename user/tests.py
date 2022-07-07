from selectors import BaseSelector
from django.urls import reverse
import pdb
from rest_framework.test import APITestCase
from rest_framework import status

from user.models import BaseUser


class UserTest(APITestCase):
    def setUp(self):
        return super().setUp()

    def test_user_registration(self):
        pass


    def test_user_update(self):
        user=BaseUser.objects.create(username='test',email='test@test.com',password='pass',is_active=True)
        user.save()

        # test user register
        url=reverse('user-register')
        data = dict(email='test1@test.com',password='password1')
        self.user=self.client.post(url,data=data)
        self.assertEqual(self.user.status_code,status.HTTP_201_CREATED)
        self.assertEqual(self.user.data,data)

        url=reverse('token-obtain')
        resp=self.client.post(url,data=dict(username='test@test.com',password='pass'),format='json')
        pdb.set_trace()

        # test user-detail
        data={
            'username':'test',
            'email':'test@test.com',
            'first_name':'test',
            'last_name':'test',
            'phone':'+9142563238'
        }
        url=reverse('user-detail',kwargs={'pk':'1'})
        resp=self.client.put(url,data=data,format='json')
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        
        # test get user-detail 
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,status.HTTP_200_OK)

        # test password-change
        url=reverse('password-change')
        data=dict(old_password='password',newpassword='new_password')
        resp=self.client.put(url,data=data,format='json')


if __name__ == '__main__':
    url='loca'