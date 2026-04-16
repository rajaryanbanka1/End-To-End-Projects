from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("data/processed/features.csv")

df = df.dropna()

X = df[['crypto_price','gdp_growth']]
y = df['stock_price']

model = LinearRegression()
model.fit(X,y)

print("Model Score:", model.score(X,y))
