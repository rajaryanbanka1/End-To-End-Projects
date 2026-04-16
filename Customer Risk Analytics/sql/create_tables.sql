-- Stock Prices
CREATE TABLE stock_prices (
    date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume BIGINT
);

-- Crypto Prices
CREATE TABLE crypto_prices (
    date DATE,
    price FLOAT
);

-- Macro Data
CREATE TABLE macro_data (
    date DATE,
    gdp_growth FLOAT
);
