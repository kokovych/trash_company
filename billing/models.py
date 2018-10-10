from django.db import models
from account.models import PersonalAccount

# Create your models here.

class Bill(models.Model):
    user_account = models.OneToOneField(PersonalAccount, on_delete=models.CASCADE)
    bill = models.FloatField(blank=True, default=0.0)
