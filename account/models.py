from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, AbstractUser
from .managers import PersonalAccountManager


class PersonalAccount(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
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
