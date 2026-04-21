-- sql/schema.sql

-- Dimension: Customers
CREATE TABLE dim_customers (
    customer_id TEXT PRIMARY KEY,
    customer_city TEXT,
    customer_state TEXT
);

-- Dimension: Products
CREATE TABLE dim_products (
    product_id TEXT PRIMARY KEY,
    product_category_name TEXT
);

-- Fact: Orders
CREATE TABLE fact_orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_purchase_timestamp TIMESTAMP,
    payment_value FLOAT
);

-- Analytics table (optional precomputed)
CREATE TABLE customer_metrics (
    customer_id TEXT,
    total_orders INT,
    total_revenue FLOAT
);