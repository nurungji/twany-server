from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..user import User


class UserTests(APITestCase):
    def create_user(self, name, nick_name, email, password):
        url = reverse('/api/v1/user/')
        data = {
            'name': name,
            'nick_name': nick_name,
            'email': email,
            'password': password
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_create_and_retrieve_user(self):
        name = 'Hyunmin Park'
        nick_name = 'Nick'
        password = '1234'
        email = 'nick.park1860@gmail.com'

        # when
        response = self.create_user(name, nick_name, email, password)

        # then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, name)
        print("PK {0}".format(User.objects.get().pk))
