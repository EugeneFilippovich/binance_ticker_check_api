import pytest

from entities.assets_dataclass import assets_config
from helpers.assets_prices import compare_with_btc


class TestBinanceApiClient:
    @pytest.mark.parametrize("cryptocurrency", assets_config.cryptocurrencies, ids=lambda c: c.name)
    def test_get_latest_price(self, api_client, cryptocurrency):
        price = api_client.get_latest_price(cryptocurrency.symbol)
        assert isinstance(price, float), f"Expected {price} to be a float"

    @pytest.mark.parametrize("cryptocurrency", assets_config.cryptocurrencies, ids=lambda c: c.name)
    def test_get_price_change_percentage(self, api_client, cryptocurrency):
        percentage_change = api_client.get_price_change_percentage(cryptocurrency.symbol)
        assert isinstance(percentage_change, float), f"Expected {percentage_change} to be a float"

    def test_tickers_is_dict(self, api_client, get_all_tickers):
        assert isinstance(get_all_tickers, dict), f"Expected {get_all_tickers} to be a dictionary"

    def test_tickers_not_empty(self, api_client, get_all_tickers):
        assert len(get_all_tickers) > 0, "Expected tickers dictionary to have at least one entry"

    def test_tickers_symbol_is_string(self, api_client, get_all_tickers):
        for symbol in get_all_tickers:
            assert isinstance(symbol, str), f"Expected {symbol} to be a string"

    def test_tickers_price_is_float(self, api_client, get_all_tickers):
        for symbol, price in get_all_tickers.items():
            assert isinstance(price, float), f"Expected {price} to be a float"

    def test_compare_with_btc_custom_ticker(self, api_client, tickers_values):
        lower_than_btc = compare_with_btc(tickers_values)
        assert isinstance(lower_than_btc, list)
        assert lower_than_btc == ["SUIUSDT", "WAVESUSDT", "APTUSDT", "ARBUSDT"]

    def test_compare_with_btc_all_ticker(self, api_client, get_all_tickers):
        # по этому тесту вопрос: через ендпоинт ticker/price я получаю все пары всех фиатов к крипте.
        # То есть там будут ценовые значения выше, чем BTCUSDT. Логика такая, но, вероятно, надо другой ендпоинт дергать
        cheaper_currencies = []
        btc_price = get_all_tickers['BTCUSDT']

        for name, price in get_all_tickers.items():
            if name != 'BTCUSDT' and price >= btc_price:
                cheaper_currencies.append(name)

        assert len(cheaper_currencies) == 0, f"Cryptocurrencies with a higher price than BTC: {cheaper_currencies}"
