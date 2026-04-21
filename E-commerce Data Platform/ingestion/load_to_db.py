# ingestion/load_to_db.py

import pandas as pd
from sqlalchemy import create_engine, text
import sys

# 🔹 DATABASE CONFIG
DB_URI = "postgresql+psycopg2://postgres:admin123@localhost:5432/postgres"

def create_tables(engine):
    """Create tables if not exists"""
    
    with engine.connect() as conn:
        
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_customers (
            customer_id TEXT PRIMARY KEY,
            customer_city TEXT,
            customer_state TEXT
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS fact_orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            order_purchase_timestamp TIMESTAMP,
            payment_value FLOAT
        );
        """))

        conn.commit()
        print("✅ Tables created")


def load_csv_to_table(engine, file_path, table_name):
    """Load CSV into PostgreSQL table"""

    try:
        df = pd.read_csv(file_path)

        print(f"📂 Loading {table_name} | Rows: {len(df)}")

        with engine.connect() as conn:
            # Clear table before loading (idempotent)
            conn.execute(text(f"TRUNCATE TABLE {table_name};"))
            conn.commit()

        # Insert data
        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=5000
        )

        print(f"✅ {table_name} loaded successfully\n")

    except Exception as e:
        print(f"❌ Error loading {table_name}: {e}")
        sys.exit(1)


def load():
    """Main load function"""

    print("🚀 Starting data load...")

    # Create DB engine
    engine = create_engine(DB_URI)

    # Create tables
    create_tables(engine)

    # Load curated files
    load_csv_to_table(engine, "F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/curated/dim_customers.csv", "dim_customers")
    load_csv_to_table(engine, "F:/Repository/End-To-End-Projects/E-commerce Data Platform//data_lake/curated/fact_orders.csv", "fact_orders")

    print("🎯 Data load complete!")


if __name__ == "__main__":
    load()