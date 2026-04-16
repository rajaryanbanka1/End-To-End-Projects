import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/features.csv")

sns.lineplot(x='date', y='stock_price', data=df)
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
