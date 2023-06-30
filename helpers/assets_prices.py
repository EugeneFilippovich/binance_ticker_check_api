def compare_with_btc(tickers: dict) -> list:
    btc_price = tickers.get("BTCUSDT", 0)
    lower_than_btc = []
    for symbol, price in tickers.items():
        if symbol != "BTCUSDT" and price < btc_price:
            lower_than_btc.append(symbol)
    return lower_than_btc
