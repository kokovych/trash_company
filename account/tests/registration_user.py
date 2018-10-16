from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

from account.models import PersonalAccount
from account.utils import TYPE_USERS


class RegistrationAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_email = "test@example.com"
        self.test_password = "Password12345"
        self.registration_url = reverse("user_registration")
    
    def test_register_user(self):
        data = {
            "email": self.test_email,
            "password": self.test_password
        }
        response = self.client.post(self.registration_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        resp_data = response.data
        self.assertEqual(PersonalAccount.objects.all().count(), 1)
        user = PersonalAccount.objects.first()
        self.assertEqual(user.email, self.test_email)
        self.assertEqual(user, Token.objects.get(key=resp_data.get('token')).user)
        self.assertEqual(TYPE_USERS[1][0], user.user_type)
    
    def test_register_without_email(self):
        data = {"password": self.test_password}
        response = self.client.post(self.registration_url, data=data)
        resp_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = resp_data['email'][0]
        self.assertTrue('field is required' in str(error))
        self.assertEqual(PersonalAccount.objects.all().count(), 0)

    def test_register_without_password(self):
        data = {"email": self.test_email}
        response = self.client.post(self.registration_url, data=data)
        resp_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = resp_data['password'][0]
        self.assertTrue('field is required' in str(error))
        self.assertEqual(PersonalAccount.objects.all().count(), 0)

    def test_register_incorrect_email(self):
        data = {
            "email": "email@email",
            "password": self.test_password
        }
        response = self.client.post(self.registration_url, data=data)
        resp_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = resp_data['email'][0]
        self.assertTrue('Enter a valid email address' in str(error))
        self.assertEqual(PersonalAccount.objects.all().count(), 0)

    def test_register_incorrect_password(self):
        data = {
            "email": self.test_email,
            "password": '12345'
        }
        response = self.client.post(self.registration_url, data=data)
        resp_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = resp_data['password'][0]
        self.assertTrue('Ensure this field has at least 8 characters' in str(error))
        self.assertEqual(PersonalAccount.objects.all().count(), 0)
