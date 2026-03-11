import pandas as pd

df = pd.read_csv("data/sales_data.csv")

print("Dataset:")
print(df)

print("\nAverage Price:")
print(df["Price"].mean())

print("\nTotal Quantity Sold:")
print(df["Quantity"].sum())

print("\nSales by Product:")
print(df.groupby("Product")["Quantity"].sum())
