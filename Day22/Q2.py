import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("sales.csv")

# Add Total column
df["Total"] = df["Quantity"] * df["Price"]

# Calculations
total_sales = np.sum(df["Total"])
average_sales = np.mean(df["Total"])
std_sales = np.std(df["Total"])

# Best selling product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()

print(df)
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation:", std_sales)
print("Best-Selling Product:", best_product)
