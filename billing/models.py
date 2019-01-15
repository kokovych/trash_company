from django.db import models
from django.utils import timezone

from account.models import PersonalAccount


class Bill(models.Model):
    user_account = models.ForeignKey(PersonalAccount, on_delete=models.CASCADE)
    bill = models.FloatField(blank=True, default=0.0)
    last_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "email:{}--bill:{}".format(
            self.user_account.email, self.user_account.personal_account_number)

    def personal_account_number(self):
        return self.user_account.personal_account_number
