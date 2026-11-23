import pandas as pd
import os

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_sales.csv")

# Convert sale_date to datetime
df["sale_date"] = pd.to_datetime(df["sale_date"])

# -------------------------------
# Date Features
# -------------------------------
df["year"] = df["sale_date"].dt.year
df["month"] = df["sale_date"].dt.month
df["day"] = df["sale_date"].dt.day
df["day_of_week"] = df["sale_date"].dt.dayofweek
df["quarter"] = df["sale_date"].dt.quarter

# Weekend Feature
df["is_weekend"] = df["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)

# -------------------------------
# Revenue Before Discount
# -------------------------------
df["gross_sales"] = df["price"] * df["quantity"]

# Discount Amount
df["discount_amount"] = (
    df["gross_sales"] * df["discount"] / 100
)

# -------------------------------
# Encode Category
# -------------------------------
df["category_code"] = (
    df["category"]
    .astype("category")
    .cat.codes
)

# -------------------------------
# Encode Region
# -------------------------------
df["region_code"] = (
    df["region"]
    .astype("category")
    .cat.codes
)

# -------------------------------
# Save Feature Engineered Dataset
# -------------------------------
output_file = "outputs/feature_engineered_sales.csv"

df.to_csv(output_file, index=False)

print("✅ Feature Engineering Completed Successfully")
print(f"📁 Saved to: {output_file}")

print("\nNew Features Added:")
print("- year")
print("- month")
print("- day")
print("- day_of_week")
print("- quarter")
print("- is_weekend")
print("- gross_sales")
print("- discount_amount")
print("- category_code")
print("- region_code")