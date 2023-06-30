import pytest

from binance_api.binance_api_client import BinanceApiClient
from entities.assets_dataclass import AssetsConfig


@pytest.fixture(scope='session')
def assets_config() -> AssetsConfig:
    return AssetsConfig()


@pytest.fixture(scope='session')
def api_client(assets_config) -> BinanceApiClient:
    return BinanceApiClient(assets_config)
