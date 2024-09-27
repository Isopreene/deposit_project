from rest_framework import serializers
from depositapp.models import DepositModel


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositModel
        fields = "__all__"
