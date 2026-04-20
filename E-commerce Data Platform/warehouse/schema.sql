-- warehouse/schema.sql
CREATE TABLE dim_customers (
    customer_id TEXT PRIMARY KEY,
    customer_city TEXT,
    customer_state TEXT
);

CREATE TABLE fact_orders (
    order_id TEXT,
    customer_id TEXT,
    payment_value FLOAT,
    order_purchase_timestamp TIMESTAMP
);