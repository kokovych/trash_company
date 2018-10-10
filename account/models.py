from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PersonalAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=150, blank=True)
    street = models.CharField(max_length=150, blank=True)
    house = models.CharField(max_length=30, blank=True)
    flat = models.CharField(max_length=15, blank=True)

    # litsevoy schet
    personal_account_number = models.CharField(max_length=30, blank=True)
