import requests
from typing import (
    Dict,
    List
)


class BinanceApiClient:
    def __init__(self, assets_config):
        self.base_url = "https://api.binance.com/api/v3"
        self.assets_config = assets_config

    def get_latest_price(self, symbol: str) -> float:
        url = f"{self.base_url}/ticker/price?symbol={symbol}"
        response = self._get(url)
        return float(response["price"])

    def get_price_change_percentage(self, symbol: str, time_range: str = "24hr") -> float:
        url = f"{self.base_url}/ticker/{time_range}?symbol={symbol}"
        response = self._get(url)
        price_change_percentage = float(response["priceChangePercent"])
        return price_change_percentage

    def get_all_tickers(self, write_to_file: bool = True, file_path: str = "tickers.txt") -> Dict[str, float]:
        url = f"{self.base_url}/ticker/price"
        response = self._get(url)
        tickers = {ticker["symbol"]: float(ticker["price"]) for ticker in response}
        if write_to_file and file_path:
            with open(file_path, "w") as file:
                for symbol, price in tickers.items():
                    file.write(f"{symbol}: {price}\n")
        return tickers

    @staticmethod
    def assets_lower_than_btc(tickers: Dict[str, float]) -> List[str]:
        btc_price = tickers.get("BTCUSDT", 0)
        lower_than_btc = [symbol for symbol, price in tickers.items() if price < btc_price]
        return lower_than_btc

    @staticmethod
    def _get(url: str) -> Dict:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exception:
            print(f"Error occurred while sending request: {exception}")
            raise exception
