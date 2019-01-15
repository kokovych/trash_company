from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from .managers import PersonalAccountManager
from .utils import TYPE_USERS


class PersonalAccount(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(max_length=255, choices=TYPE_USERS,
    blank=True, null=True, default=TYPE_USERS[1][0])
    city = models.CharField(max_length=150, blank=True)
    street = models.CharField(max_length=150, blank=True)
    house = models.CharField(max_length=30, blank=True)
    flat = models.CharField(max_length=15, blank=True)
    # litsevoy schet
    personal_account_number = models.CharField(max_length=30, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PersonalAccountManager()

    class Meta:
        verbose_name = 'Personal Account'
        verbose_name_plural = 'Personal Accounts'


def create_auth_token(instance=None, created=False, **_):
    if created:
        Token.objects.create(user=instance)


def create_username_default(instance=None, created=False, **_):
    if created:
        user = instance
        username = user.username
        if not username:
            email = user.email
            user.username = email
            user.save()


def create_personal_account_default(instance=None, created=False, **_):
    if created:
        user = instance
        user_id = user.id
        personal_account_number = "000000000" + str(user_id)
        if len(personal_account_number) > 9:
            diff = len(personal_account_number) - 9
            personal_account_number = personal_account_number[diff:]
            user.personal_account_number = personal_account_number
        else:
            user.personal_account_number = user_id
        user.save()


post_save.connect(create_auth_token, sender=settings.AUTH_USER_MODEL)
post_save.connect(create_username_default, sender=settings.AUTH_USER_MODEL)
post_save.connect(create_personal_account_default, sender=settings.AUTH_USER_MODEL)