-- Risk-adjusted performance score

SELECT 
    AVG(stock_return) AS avg_return,
    STDDEV(stock_return) AS risk,
    
    AVG(stock_return) / NULLIF(STDDEV(stock_return),0) AS sharpe_ratio
FROM features;
