# Generated by Django 2.1.2 on 2018-10-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalaccount',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Customer', 'Customer')], default='Customer', max_length=255, null=True),
        ),
    ]
