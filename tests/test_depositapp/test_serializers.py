import pytest
from depositapp.serializers import DepositSerializer
from tests.test_depositapp.test_data import get_valid_test_data, get_invalid_test_data_missing_date


def test_valid_deposit_serializer(get_valid_test_data):
    serializer = DepositSerializer(data=get_valid_test_data)
    assert isinstance(serializer, DepositSerializer)
    assert serializer.is_valid()
    assert serializer.validated_data == get_valid_test_data
    assert serializer.data == get_valid_test_data
    assert serializer.errors == {}

def test_invalid_deposit_serializer(get_invalid_test_data_missing_date):
    serializer = DepositSerializer(data=get_invalid_test_data_missing_date)
    assert isinstance(serializer, DepositSerializer)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == get_invalid_test_data_missing_date
    assert serializer.errors == {"date": ["Обязательное поле."]}