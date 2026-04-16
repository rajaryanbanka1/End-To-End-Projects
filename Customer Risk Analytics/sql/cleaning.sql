-- Remove nulls and ensure valid values

CREATE TABLE stock_cleaned AS
SELECT *
FROM stock_prices
WHERE close IS NOT NULL;

CREATE TABLE crypto_cleaned AS
SELECT *
FROM crypto_prices
WHERE price > 0;

CREATE TABLE macro_cleaned AS
SELECT *
FROM macro_data
WHERE gdp_growth IS NOT NULL;
