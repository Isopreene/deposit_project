from rest_framework import serializers

from depositapp.models import DepositModel
from depositapp.validators import DepositValidator

class DepositSerializer(serializers.ModelSerializer, DepositValidator):
    class Meta:
        model = DepositModel
        fields = ["date", "periods", "amount", "rate"]