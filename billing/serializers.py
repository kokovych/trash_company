from rest_framework import serializers

from .models import Bill
from account.serializers import PersonalAccountSerializer


class BillSerializer(serializers.ModelSerializer):
    user_account = PersonalAccountSerializer()

    class Meta:
        model = Bill
        fields = "__all__"

