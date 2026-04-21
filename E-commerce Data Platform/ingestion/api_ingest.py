import requests
import pandas as pd
import os

def fetch_api_data():
    url = "https://fakestoreapi.com/products"
    
    # Fetch data from API
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data)
    
    # Save to data lake (raw)
    os.makedirs("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/raw", exist_ok=True)
    df.to_csv("F:/Repository/End-To-End-Projects/E-commerce Data Platform/data_lake/raw/products.csv")
    
    print("API data ingested successfully")

if __name__ == "__main__":
    fetch_api_data()