import pytest
from depositapp.models import DepositModel
from tests.test_depositapp.test_data import get_valid_test_data


@pytest.mark.django_db
def test_deposit_model(get_valid_test_data):
    deposit = DepositModel(date=get_valid_test_data["date"],
                           periods=get_valid_test_data["periods"],
                           amount=get_valid_test_data["amount"],
                           rate=get_valid_test_data["rate"])
    deposit.save()
    assert isinstance(deposit, DepositModel)
    assert deposit.date == get_valid_test_data["date"]
    assert deposit.periods == get_valid_test_data["periods"]
    assert deposit.amount == get_valid_test_data["amount"]
    assert deposit.rate == get_valid_test_data["rate"]
    assert len(deposit.date) <= 10