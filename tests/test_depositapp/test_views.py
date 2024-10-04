import pytest
from depositapp.models import DepositModel
from tests.test_depositapp.test_data import (get_valid_calculate_deposit,
                                             get_valid_test_data,
                        get_invalid_test_data)
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_add_deposit(client,
                     get_valid_test_data,
                     get_valid_calculate_deposit):
    deposit = DepositModel.objects.all()
    assert len(deposit) == 0
    response = client.post("/deposit/",
                           data=get_valid_test_data)
    assert response.status_code == 200
    assert response.data["info"] == get_valid_calculate_deposit

@pytest.mark.django_db
def test_fake_deposit(client,
                     get_invalid_test_data,
                     get_valid_calculate_deposit):
    deposit = DepositModel.objects.all()
    assert len(deposit) == 0
    response = client.post("/deposit/",
                           data=get_invalid_test_data,
                           content_type='application/json')
    assert response.status_code == 400
    print(response.data["error"])
    assert bool(response.data["error"]) is True
