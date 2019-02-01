import pytest
from random import seed, randint
from datetime import datetime

seed(datetime.now())


@pytest.fixture
def get_random_int():
    return randint(1025, 2048)


def check_error_response(response):
    assert "wrong parameter" in response.text


def check_double(response, the_number):
    response = response.json()
    result = response["double"]
    assert result == int(the_number)*2
