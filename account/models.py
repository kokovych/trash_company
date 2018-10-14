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

post_save.connect(create_auth_token, sender=settings.AUTH_USER_MODEL)