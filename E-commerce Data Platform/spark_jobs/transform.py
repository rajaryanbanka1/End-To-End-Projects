# Pandas version for compatibility

import pandas as pd
import os

def process_data():
    os.makedirs("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/processed", exist_ok=True)

    orders = pd.read_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/raw/orders.csv")
    customers = pd.read_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/raw/customers.csv")

    # Clean orders
    orders = orders.drop_duplicates()
    orders['order_purchase_timestamp'] = pd.to_datetime(
        orders['order_purchase_timestamp']
    )

    # Clean customers
    customers = customers.drop_duplicates()

    # Save processed
    orders.to_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/processed/clean_orders.csv", index=False)
    customers.to_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/processed/clean_customers.csv", index=False)

    print("Processing complete")

if __name__ == "__main__":
    process_data()