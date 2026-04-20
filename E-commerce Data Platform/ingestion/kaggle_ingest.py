import pandas as pd
import os

def load_kaggle():
    os.makedirs("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/raw", exist_ok=True)

    files = {
        "orders": "olist_orders_dataset.csv",
        "customers": "olist_customers_dataset.csv",
        "products": "olist_products_dataset.csv",
        "payments": "olist_order_payments_dataset.csv",
        "order_items": "olist_order_items_dataset.csv"
    }

    for name, file in files.items():
        df = pd.read_csv(f"F:/Repository/End-To-End-Projects/E-commerce Data Platform/data/{file}")
        df.to_csv(f"F:/Repository/End-To-End-Projects/E-commerce Data Platform//data_lake/raw/{name}.csv", index=False)
        print(f"{name} loaded")

if __name__ == "__main__":
    load_kaggle()