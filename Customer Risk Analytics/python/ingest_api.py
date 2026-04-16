import requests
import pandas as pd

# ---------- STOCK DATA ----------
API_KEY = "ALPHA_VANTAGE_KEY"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey={API_KEY}"

data = requests.get(url).json()
stock_df = pd.DataFrame(data['Time Series (Daily)']).T
stock_df.to_csv("data/raw/stocks/aapl.csv")


# ---------- CRYPTO DATA ----------
crypto_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
crypto_data = requests.get(crypto_url).json()

crypto_df = pd.DataFrame(crypto_data['prices'], columns=['timestamp','price'])
crypto_df.to_csv("data/raw/crypto/btc.csv")


# ---------- MACRO DATA ----------
macro_url = "http://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.KD.ZG?format=json"

macro_data = requests.get(macro_url).json()
macro_df = pd.DataFrame(macro_data[1])
macro_df.to_csv("data/raw/macro/gdp.csv")
