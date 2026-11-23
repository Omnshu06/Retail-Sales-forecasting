import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -------------------------------------------------
# Create folders
# -------------------------------------------------
os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
try:
    df = pd.read_csv("outputs/feature_engineered_sales.csv")
except FileNotFoundError:
    print("Feature engineered dataset not found!")
    exit()

# -------------------------------------------------
# Select Features
# -------------------------------------------------
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
target = "sales"

X = df[features]
y = df[target]

# -------------------------------------------------
# Train Test Split
# -------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -------------------------------------------------
# Machine Learning Models
# -------------------------------------------------
models = {
    "Linear Regression": LinearRegression(),

    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42
    )
}

results = []

best_model = None
best_name = ""
best_r2 = float("-inf")
best_prediction = None

print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

# -------------------------------------------------
# Train Every Model
# -------------------------------------------------
for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    mae = mean_absolute_error(y_test, prediction)

    mse = mean_squared_error(y_test, prediction)
    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, prediction)

    print(f"\n{name}")
    print("-" * 40)
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R²   : {r2:.4f}")

    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2 Score": r2
    })

    if r2 > best_r2:
        best_r2 = r2
        best_model = model
        best_name = name
        best_prediction = prediction

# -------------------------------------------------
# Save Model
# -------------------------------------------------
joblib.dump(best_model, "models/sales_forecast.pkl")

# -------------------------------------------------
# Save Model Comparison
# -------------------------------------------------
results_df = pd.DataFrame(results)

results_df.to_csv(
    "outputs/model_results.csv",
    index=False
)

# -------------------------------------------------
# Actual vs Predicted Graph
# -------------------------------------------------
plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    best_prediction,
    alpha=0.7
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title(f"Actual vs Predicted ({best_name})")

plt.tight_layout()

plt.savefig("outputs/actual_vs_predicted.png")

plt.close()

# -------------------------------------------------
# Feature Importance
# -------------------------------------------------
if hasattr(best_model, "feature_importances_"):

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": best_model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    importance.to_csv(
        "outputs/feature_importance.csv",
        index=False
    )

    plt.figure(figsize=(9,5))

    plt.bar(
        importance["Feature"],
        importance["Importance"]
    )

    plt.xticks(rotation=45)

    plt.title("Feature Importance")

    plt.tight_layout()

    plt.savefig("outputs/feature_importance.png")

    plt.close()

# -------------------------------------------------
# Final Output
# -------------------------------------------------
print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Model : {best_name}")
print(f"R² Score : {best_r2:.4f}")

print("\nModel Saved Successfully")
print("models/sales_forecast.pkl")

print("\nGenerated Files")

print("outputs/model_results.csv")
print("outputs/actual_vs_predicted.png")

if hasattr(best_model, "feature_importances_"):
    print("outputs/feature_importance.csv")
    print("outputs/feature_importance.png")