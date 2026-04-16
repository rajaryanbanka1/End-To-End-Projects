-- Merge datasets on date

CREATE TABLE merged_data AS
SELECT 
    s.date,
    s.close AS stock_price,
    c.price AS crypto_price,
    m.gdp_growth
FROM stock_cleaned s
LEFT JOIN crypto_cleaned c
ON s.date = c.date
LEFT JOIN macro_cleaned m
ON s.date = m.date;
