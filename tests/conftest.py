import pytest
from binance_api.binance_api_client import BinanceApiClient
from entities.assets_dataclass import AssetsConfig


@pytest.fixture(scope='session')
def assets_config() -> AssetsConfig:
    return AssetsConfig()


@pytest.fixture(scope='session')
def api_client(assets_config) -> BinanceApiClient:
    return BinanceApiClient(assets_config)


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
