# Generated by Django 2.1.2 on 2018-10-13 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_bill_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='user_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
