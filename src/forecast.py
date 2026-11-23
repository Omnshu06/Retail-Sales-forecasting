import os
import joblib
import pandas as pd

# ---------------------------------
# Create outputs folder
# ---------------------------------
os.makedirs("outputs", exist_ok=True)

# ---------------------------------
# Load trained model
# ---------------------------------
model = joblib.load("models/sales_forecast.pkl")

# ---------------------------------
# Load feature engineered dataset
# ---------------------------------
df = pd.read_csv("outputs/feature_engineered_sales.csv")

# ---------------------------------
# Features
# Must exactly match train_model.py
# ---------------------------------
features = [
    "price",
    "quantity",
    "discount",
    "month",
    "day_of_week",
    "quarter",
    "is_weekend",
    "category_code",
    "region_code"
]

X = df[features]

# ---------------------------------
# Predict
# ---------------------------------
df["predicted_sales"] = model.predict(X)

# ---------------------------------
# Save
# ---------------------------------
df.to_csv("outputs/predictions.csv", index=False)

print("=" * 50)
print("SALES FORECAST COMPLETED")
print("=" * 50)

print(df[["sales", "predicted_sales"]].head())

print("\nPredictions saved to outputs/predictions.csv")