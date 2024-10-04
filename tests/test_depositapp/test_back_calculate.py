import pytest
from depositapp.back.calculate import calculate_deposit
from tests.test_depositapp.test_data import get_valid_calculate_deposit, get_valid_test_data
from datetime import datetime


def test_calculate_deposit(get_valid_test_data,
                           get_valid_calculate_deposit):
    assert (calculate_deposit(**get_valid_test_data) ==
            get_valid_calculate_deposit)
