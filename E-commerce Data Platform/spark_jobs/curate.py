# spark_jobs/curate.py

import pandas as pd
import os

def create_curated():
    os.makedirs("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/curated", exist_ok=True)

    orders = pd.read_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/processed/clean_orders.csv")
    customers = pd.read_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/processed/clean_customers.csv")
    payments = pd.read_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/raw/payments.csv")

    # FACT TABLE
    fact_orders = orders.merge(payments, on="order_id", how="left")

    # DIM TABLES
    dim_customers = customers.copy()

    # CUSTOMER METRICS
    customer_metrics = fact_orders.groupby("customer_id").agg({
        "payment_value": ["sum", "count"]
    }).reset_index()

    customer_metrics.columns = ["customer_id", "total_spent", "total_orders"]

    # Save curated
    fact_orders.to_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/curated/fact_orders.csv", index=False)
    dim_customers.to_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/curated/dim_customers.csv", index=False)
    customer_metrics.to_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/curated/customer_metrics.csv", index=False)

    print("Curated layer created")

if __name__ == "__main__":
    create_curated()