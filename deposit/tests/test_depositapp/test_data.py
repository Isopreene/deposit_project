import pytest


@pytest.fixture
def get_valid_test_data():
    date = "01.01.2024"
    periods = 3
    amount = 10000
    rate = 6
    return {"date": date,
            "periods": periods,
            "amount": amount,
            "rate": rate}

@pytest.fixture
def get_invalid_test_data_missing_date():
    periods = 3
    amount = 10000
    rate = 6
    return {"periods": periods,
            "amount": amount,
            "rate": rate}

@pytest.fixture
def get_invalid_test_data():
    date = "01.31.2024"
    periods = 100
    amount = 10000000
    rate = 60
    return {"date": date,
            "periods": periods,
            "amount": amount,
            "rate": rate}

@pytest.fixture
def get_valid_calculate_deposit():
    return {
        "2024-01-01": 10000.0,
        "2024-02-01": 10050.0,
        "2024-03-01": 10100.25,
        "2024-04-01": 10150.75}
