-- Add derived features

CREATE TABLE features AS
SELECT 
    *,
    
    -- Daily returns
    (stock_price - LAG(stock_price) OVER (ORDER BY date)) / stock_price AS stock_return,
    
    (crypto_price - LAG(crypto_price) OVER (ORDER BY date)) / crypto_price AS crypto_return,
    
    -- Volatility proxy
    ABS(stock_price - LAG(stock_price) OVER (ORDER BY date)) AS volatility

FROM merged_data;
