from datetime import datetime
from random import randint, seed
from typing import Union

import pytest
from requests.models import Response

seed(datetime.now())


@pytest.fixture
def get_random_int() -> int:
    return randint(1025, 2048)


def check_error_response(response: Response) -> None:
    assert "wrong parameter" in response.text


def check_double(response: Response, the_number: Union[str, int]) -> None:
    response = response.json()
    result = response["double"]
    assert result == int(the_number)*2
