# 🛒 E-Commerce Data Platform (End-to-End Data Project)

## 📌 Overview

This project demonstrates an **end-to-end data engineering and analytics workflow** using real-world e-commerce data.

It covers:

* Data ingestion from multiple sources
* Data lake architecture (raw → processed → curated)
* Data transformation using Python
* Data warehousing using PostgreSQL
* Business analytics using SQL
* Visualization using Power BI

---

## 🧠 Business Problem

E-commerce companies need to:

* Track revenue and sales trends
* Understand customer behavior
* Identify high-value customers
* Analyze regional performance

This project builds a **scalable data pipeline** to generate actionable insights.

---

## 🏗️ Architecture

```
Data Sources (Kaggle + API)
        ↓
Python Ingestion
        ↓
Data Lake (CSV)
raw → processed → curated
        ↓
Python Transformations
        ↓
PostgreSQL Warehouse
        ↓
SQL Analytics
        ↓
Power BI Dashboard
```

---

## 📁 Project Structure

```
ecommerce-data-platform/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── curated/
│
├── ingestion/
│   ├── kaggle_ingest.py
│   ├── api_ingest.py
│   └── load_to_db.py
│
├── processing/
│   ├── transform.py
│   └── curate.py
│
├── sql/
│   ├── schema.sql
│   └── analytics.sql
│
├── pipeline/
│   └── run_pipeline.py
│
├── powerbi/
│   └── dashboard.pbix
│
├── requirements.txt
└── README.md
```

---

## 🔄 Data Pipeline Workflow

1. **Ingestion**

   * Load Kaggle dataset (multiple CSVs)
   * Fetch product data via API
   * Store in `data/raw/`

2. **Processing**

   * Clean and standardize data
   * Handle missing values
   * Store in `data/processed/`

3. **Curated Layer**

   * Build fact and dimension tables
   * Generate aggregated metrics
   * Store in `data/curated/`

4. **Data Warehouse**

   * Load curated data into PostgreSQL

5. **Analytics**

   * Execute SQL queries for insights

6. **Visualization**

   * Build dashboard in Power BI

---

## 🧱 Data Model

### Fact Table

* `fact_orders`

### Dimension Tables

* `dim_customers`
* `dim_products`

### Aggregated Tables

* `customer_metrics`

---

## 📊 Key Analytics

* Revenue and order trends
* Customer segmentation
* Top customers by revenue
* Regional performance
* Cohort and time-based analysis

---

## ⚙️ Tech Stack

* Python (Pandas)
* SQL (PostgreSQL)
* Data Processing (Python scripts)
* Visualization (Power BI)

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run pipeline

```bash
python pipeline/run_pipeline.py
```

### 3. Run SQL analytics

Execute queries from:

```
sql/analytics.sql
```

---

## 🗄️ Database Setup

Make sure PostgreSQL is running.

Create database:

```sql
CREATE DATABASE ecommerce;
```

Update connection string in:

```
ingestion/load_to_db.py
```

---

## 📊 Power BI Dashboard

Connect Power BI to PostgreSQL and build:

* KPI cards (Revenue, Orders)
* Monthly revenue trend
* Top customers chart
* Revenue by region map

---

## 🚀 Future Improvements

* Incremental data loading
* Real-time data pipeline
* Cloud deployment (AWS / Azure / GCP)
* Data validation & logging

---

## 👨‍💻 Author

Raj Aryan Banka
Data Analyst / Data Engineering Portfolio Project
