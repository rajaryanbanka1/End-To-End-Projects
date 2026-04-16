import pandas as pd

# -----------------------------
# STOCK DATA CLEANING
# -----------------------------
def preprocess_stock(file_path):
    df = pd.read_csv(file_path)

    # Flatten column names from API format
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Convert date
    df['date'] = pd.to_datetime(df['date'])

    # Convert numeric columns
    numeric_cols = ['open', 'high', 'low', 'close', 'volume']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove duplicates
    df = df.drop_duplicates()

    return df


# -----------------------------
# CRYPTO DATA CLEANING
# -----------------------------
def preprocess_crypto(df):
    df = df.copy()

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.rename(columns={'timestamp': 'date'}, inplace=True)

    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df = df.drop_duplicates()

    return df


# -----------------------------
# SAVE CLEAN OUTPUTS
# -----------------------------
if __name__ == "__main__":
    stock = preprocess_stock("data/raw/stocks/aapl.csv")
    crypto = pd.read_csv("data/raw/crypto/btc.csv")

    crypto = preprocess_crypto(crypto)

    stock.to_csv("data/staging/stock_clean.csv", index=False)
    crypto.to_csv("data/staging/crypto_clean.csv", index=False)
