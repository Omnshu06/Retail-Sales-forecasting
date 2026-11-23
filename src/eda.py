import os
import pandas as pd
import matplotlib.pyplot as plt

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_sales.csv")

# Convert sale_date to datetime
df["sale_date"] = pd.to_datetime(df["sale_date"])

# -------------------------------
# Monthly Sales Trend
# -------------------------------
monthly_sales = (
    df.groupby(df["sale_date"].dt.to_period("M"))["sales"]
    .sum()
)

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")
plt.close()

# -------------------------------
# Sales by Category
# -------------------------------
category_sales = df.groupby("category")["sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/category_sales.png")
plt.close()

# -------------------------------
# Sales by Region
# -------------------------------
region_sales = df.groupby("region")["sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/region_sales.png")
plt.close()

# -------------------------------
# Discount vs Sales
# -------------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["discount"], df["sales"], alpha=0.5)
plt.title("Discount vs Sales")
plt.xlabel("Discount")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/discount_vs_sales.png")
plt.close()

# -------------------------------
# Quantity Distribution
# -------------------------------
plt.figure(figsize=(8,5))
plt.hist(df["quantity"], bins=20)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("outputs/quantity_distribution.png")
plt.close()

# -------------------------------
# Top 10 Products
# -------------------------------
top_products = (
    df.groupby("product_id")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product ID")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/top_products.png")
plt.close()

print("✅ EDA completed successfully!")
print("📊 Graphs saved in outputs/")