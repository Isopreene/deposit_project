import pytest
from tests.test_depositapp.test_data import *
from depositapp.validators import DepositValidator
from rest_framework.serializers import ValidationError

validator = DepositValidator()
assert isinstance(validator, DepositValidator)

def test_deposit_validator_date(get_valid_test_data,
                            get_invalid_test_data):
    assert validator.validate_date(get_valid_test_data["date"]) is get_valid_test_data["date"]
    with pytest.raises(ValidationError):
        validator.validate_date(get_invalid_test_data[
                                           "date"])

def test_deposit_validator_periods(get_valid_test_data,
                            get_invalid_test_data):
    assert (validator.validate_periods(get_valid_test_data["periods"]) is
            get_valid_test_data["periods"])
    with pytest.raises(ValidationError):
        validator.validate_periods(get_invalid_test_data[
                                           "periods"])

def test_deposit_validator_amount(get_valid_test_data,
                            get_invalid_test_data):
    assert (validator.validate_amount(get_valid_test_data["amount"]) is
            get_valid_test_data["amount"])
    with pytest.raises(ValidationError):
        validator.validate_amount(get_invalid_test_data[
                                           "amount"])

def test_deposit_validator_rate(get_valid_test_data,
                            get_invalid_test_data):
    assert (validator.validate_rate(get_valid_test_data["rate"]) is
            get_valid_test_data["rate"])
    with pytest.raises(ValidationError):
        validator.validate_rate(get_invalid_test_data[
                                           "rate"])