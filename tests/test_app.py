import requests
from unittest import mock


def add_7_numbers(*args):
    # print(args)
    return sum(args)


def get_current_price(symbol):
    url = "https://blockchain.info/ticker"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        usd = result["USD"]["last"]
        return usd
    return None


class FakeResponse:
    def __init__(self, status_code, result) -> None:
        self.status_code = status_code
        self.result = result

    def json(self):
        return self.result


def test_can_add_7_numbers():
    result = add_7_numbers(1, 2, 3, 4, 5, 6, 7)
    assert result == 28


def test_get_current_price_of_bitcoin(mocker):
    fake_request = mocker.patch("requests.get")
    fake_request.return_value = FakeResponse(200, {"USD": {"last": 62000}})
    price = get_current_price("BTCUSD")
    assert price != None
    assert price == 62000
    fake_request.assert_called_with("https://blockchain.info/ticker")
