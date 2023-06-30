import pytest


@pytest.fixture(scope='class')
def tickers_values() -> dict:
    return {
        "BTCUSDT": 50000,
        "SUIUSDT": 2000,
        "WAVESUSDT": 300,
        "APTUSDT": 1,
        "ARBUSDT": 0.5
    }


@pytest.fixture(scope='class')
def get_all_tickers(api_client) -> dict:
    return api_client.get_all_tickers()
