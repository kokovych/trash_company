from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from .models import PersonalAccount


class PersonalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalAccount
        exclude = ("password", "groups", "user_permissions", "last_login", "date_joined")


class CreatePersonalAccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=PersonalAccount.objects.all()
        )]
    )
    password = serializers.CharField(min_length=8)

    class Meta:
        model = PersonalAccount
        fields = 'email', 'password'

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = PersonalAccount.objects.create_user(
            email=email, password=password 
        )
        return user
