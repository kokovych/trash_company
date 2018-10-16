from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError
from time import sleep

from account.models import PersonalAccount
from account.utils import TYPE_USERS
# from .utils import TYPE_USERS


class AccountCreateUserTest(TestCase):
    def setUp(self):
        self.user_email_1 = 'test_01@example.com'
        self.user_email_2 = 'test_02@example.com'
        self.user_password_1 = 'password123'
        self.user_password_2 = 'password12345'
        self.username_1 = 'test_username1'
        self.username_2 = 'test_username2'
    
    def test_create_user(self):
        user_test = PersonalAccount.objects.create_user(
            email=self.user_email_1,
            password=self.user_password_1
        )
        total_users = PersonalAccount.objects.all().count()
        self.assertEqual(total_users, 1)
        self.assertEqual(user_test.email, self.user_email_1)
        self.assertFalse(user_test.is_superuser)
        self.assertFalse(user_test.is_staff)
        self.assertEqual(user_test.user_type, TYPE_USERS[1][0])

    def test_create_superuser(self):
        test_su = PersonalAccount.objects.create_superuser(
            email=self.user_email_1,
            password=self.user_password_1
        )
        self.assertEqual(test_su.email, self.user_email_1)
        self.assertTrue(test_su.is_superuser)
        self.assertTrue(test_su.is_staff)
        self.assertEqual(test_su.user_type, TYPE_USERS[0][0])
        
        
    def test_create_user_without_email(self):
        try:
            PersonalAccount.objects.create_user(
                password=self.user_password_1
            )
        except TypeError as e:
            error_test = str(e)
            self.assertEqual("create_user() missing 1 required positional argument: 'email'", error_test)
    
    def test_create_user_unique_email(self):
        user1 = PersonalAccount.objects.create_user(
            email=self.user_email_1,
            password=self.user_password_1,
            username = self.username_1
        )
        try:
            # Duplicates should be prevented.
            with transaction.atomic():
                user2 = PersonalAccount.objects.create_user(
                    email=self.user_email_1,
                    password=self.user_password_2,
                    username=self.username_2
                )
        except IntegrityError as e:
            error_text = str(e)
            self.assertTrue("(test_01@example.com) already exists" in error_text)
        finally:
            total_users = PersonalAccount.objects.all().count()
            self.assertEqual(total_users, 1)
            self.assertEqual(self.user_email_1, user1.email)
            self.assertEqual(self.username_1, user1.username)

    def test_create_user_unique_username(self):
        user1 = PersonalAccount.objects.create_user(
            email=self.user_email_1,
            password=self.user_password_1,
            username = self.username_1
        )
        try:
            # Duplicates should be prevented.
            with transaction.atomic():
                user2 = PersonalAccount.objects.create_user(
                    email=self.user_email_2,
                    password=self.user_password_2,
                    username=self.username_1
                )
        except IntegrityError as e:
            error_text = str(e)
            self.assertTrue("(%s) already exists" % self.username_1 in error_text)
        finally:
            total_users = PersonalAccount.objects.all().count()
            self.assertEqual(total_users, 1)
            self.assertEqual(self.user_email_1, user1.email)
            self.assertEqual(self.username_1, user1.username)
