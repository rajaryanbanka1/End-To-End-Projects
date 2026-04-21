-- =========================================
-- 1. OVERALL BUSINESS METRICS
-- =========================================

-- Total Revenue
SELECT SUM(payment_value) AS total_revenue
FROM fact_orders;

-- Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM fact_orders;

-- Average Order Value (AOV)
SELECT 
    SUM(payment_value) / COUNT(DISTINCT order_id) AS avg_order_value
FROM fact_orders;

-- Unique Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM fact_orders;

-- Revenue per Customer
SELECT 
    SUM(payment_value) / COUNT(DISTINCT customer_id) AS revenue_per_customer
FROM fact_orders;

--------------------------------------------------

-- =========================================
-- 2. TIME-BASED ANALYSIS
-- =========================================

-- Monthly Revenue Trend
SELECT 
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    SUM(payment_value) AS revenue
FROM fact_orders
GROUP BY month
ORDER BY month;

-- Monthly Orders Trend
SELECT 
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    COUNT(order_id) AS orders
FROM fact_orders
GROUP BY month
ORDER BY month;

-- Growth Rate (Month-over-Month)
WITH monthly AS (
    SELECT 
        DATE_TRUNC('month', order_purchase_timestamp) AS month,
        SUM(payment_value) AS revenue
    FROM fact_orders
    GROUP BY month
)
SELECT 
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
    (revenue - LAG(revenue) OVER (ORDER BY month)) 
        / LAG(revenue) OVER (ORDER BY month) AS growth_rate
FROM monthly;

--------------------------------------------------

-- =========================================
-- 3. CUSTOMER ANALYTICS
-- =========================================

-- Customer Lifetime Value (CLV)
SELECT 
    customer_id,
    SUM(payment_value) AS lifetime_value
FROM fact_orders
GROUP BY customer_id
ORDER BY lifetime_value DESC;

-- Repeat vs One-time Customers
SELECT 
    CASE 
        WHEN COUNT(order_id) = 1 THEN 'One-time'
        ELSE 'Repeat'
    END AS customer_type,
    COUNT(*) AS num_customers
FROM (
    SELECT customer_id, COUNT(order_id) AS order_count
    FROM fact_orders
    GROUP BY customer_id
) t
GROUP BY customer_type;

-- Top 10 Customers
SELECT 
    customer_id,
    SUM(payment_value) AS revenue
FROM fact_orders
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 10;

--------------------------------------------------

-- =========================================
-- 4. GEOGRAPHICAL ANALYTICS
-- =========================================

-- Revenue by State
SELECT 
    d.customer_state,
    SUM(f.payment_value) AS revenue
FROM fact_orders f
JOIN dim_customers d
ON f.customer_id = d.customer_id
GROUP BY d.customer_state
ORDER BY revenue DESC;

-- Orders by State
SELECT 
    d.customer_state,
    COUNT(f.order_id) AS total_orders
FROM fact_orders f
JOIN dim_customers d
ON f.customer_id = d.customer_id
GROUP BY d.customer_state
ORDER BY total_orders DESC;

--------------------------------------------------

-- =========================================
-- 5. PRODUCT ANALYTICS
-- =========================================

-- Top Products by Revenue
SELECT 
    oi.product_id,
    SUM(oi.price) AS revenue
FROM order_items oi
GROUP BY oi.product_id
ORDER BY revenue DESC
LIMIT 10;

-- Product Popularity
SELECT 
    product_id,
    COUNT(order_id) AS times_ordered
FROM order_items
GROUP BY product_id
ORDER BY times_ordered DESC;

--------------------------------------------------

-- =========================================
-- 6. ADVANCED SEGMENTATION (🔥 IMPORTANT)
-- =========================================

-- RFM Segmentation (Recency, Frequency, Monetary)

WITH rfm AS (
    SELECT 
        customer_id,
        MAX(order_purchase_timestamp) AS last_purchase,
        COUNT(order_id) AS frequency,
        SUM(payment_value) AS monetary
    FROM fact_orders
    GROUP BY customer_id
)
SELECT *,
    CASE 
        WHEN monetary > 1000 THEN 'High Value'
        WHEN monetary > 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS segment
FROM rfm;

--------------------------------------------------

-- =========================================
-- 7. COHORT ANALYSIS (🔥 ADVANCED)
-- =========================================

WITH first_purchase AS (
    SELECT 
        customer_id,
        MIN(DATE_TRUNC('month', order_purchase_timestamp)) AS cohort_month
    FROM fact_orders
    GROUP BY customer_id
),
activity AS (
    SELECT 
        f.customer_id,
        DATE_TRUNC('month', f.order_purchase_timestamp) AS activity_month,
        fp.cohort_month
    FROM fact_orders f
    JOIN first_purchase fp
    ON f.customer_id = fp.customer_id
)
SELECT 
    cohort_month,
    activity_month,
    COUNT(DISTINCT customer_id) AS active_users
FROM activity
GROUP BY cohort_month, activity_month
ORDER BY cohort_month, activity_month;

--------------------------------------------------

-- =========================================
-- 8. OPERATIONAL METRICS
-- =========================================

-- Daily Orders
SELECT 
    DATE(order_purchase_timestamp) AS day,
    COUNT(order_id) AS orders
FROM fact_orders
GROUP BY day
ORDER BY day;

-- Peak Sales Day
SELECT 
    DATE(order_purchase_timestamp) AS day,
    SUM(payment_value) AS revenue
FROM fact_orders
GROUP BY day
ORDER BY revenue DESC
LIMIT 1;

--------------------------------------------------

-- =========================================
-- 9. DATA QUALITY CHECKS
-- =========================================

-- Null checks
SELECT COUNT(*) FROM fact_orders WHERE customer_id IS NULL;

-- Duplicate orders
SELECT order_id, COUNT(*)
FROM fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;