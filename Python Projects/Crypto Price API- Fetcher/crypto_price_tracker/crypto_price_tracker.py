def get_btc_price(currency):
    import requests

    url = "https://api.coingecko.com/api/v3/simple/price"
    parameters = {"ids": "bitcoin", "vs_currencies": currency}
    btcResponse = requests.get(url, params= parameters, timeout= 10)
    btcData = btcResponse.json()
    btcPrice = btcData["bitcoin"][currency]
    return btcPrice


def get_eth_price(currency):
    import requests

    url = "https://api.coingecko.com/api/v3/simple/price"
    ethParameters = {"ids": "ethereum", "vs_currencies": currency}
    ethResponse = requests.get(url, params= ethParameters, timeout= 10)
    ethData = ethResponse.json()
    ethPrice = ethData["ethereum"][currency]
    return ethPrice


userChoiceCoin = input ("Would you like to see the price of btc or eth? ").upper()
userChoiceCurrency = input ("Which currency would you like to convert into, USD or GBP? ").lower()

currency_symbols = {"gbp": "£", "usd": "$"}
symbol = currency_symbols.get(userChoiceCurrency, " ")

if userChoiceCoin == "BTC":
    btcGetPrice = get_btc_price(userChoiceCurrency)
    print(f"Value of a Bitcoin right now: {symbol}{btcGetPrice:,}")

elif userChoiceCoin == "ETH":
    ethGetPrice = get_eth_price(userChoiceCurrency)
    print(f"Value of an ethereum right now: {symbol}{ethGetPrice:,}")

