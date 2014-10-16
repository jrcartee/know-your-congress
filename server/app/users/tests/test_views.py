# Django Imports
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model
# REST-Framework Imports
from rest_framework.authtoken.models import Token
# Testing Imports
User = get_user_model()


ROOT_URL = 'http://127.0.0.1:8000/users'


class Login(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = ROOT_URL + '/login/'
        self.data = {
            'email': "testuser@inbox.com",
            'password': 'testpass'
        }
        user = User.objects.create_user(
            email=self.data['email'],
            password=self.data['password'],
            first_name="Joe",
            last_name="Schmo"
        )
        Token.objects.create(user=user)

    def test_basic(self):
        response = self.client.post(self.url, self.data)
        assert response.status_code == 200, response.content


class Register(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {
            'email': 'testuser@inbox.com',
            'password1': 'testpass',
            'password2': 'testpass',
            'first_name': 'Joe',
            'last_name': 'Schmo'
        }
        self.url = ROOT_URL + '/register/'

    def test_basic(self):
        response = self.client.post(self.url, self.data)
        assert response.status_code == 200

        User.objects.get(email=self.data['email'])
