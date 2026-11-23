import subprocess

steps = [
    "python -m src.load_data",
    "python -m src.preprocessing",
    "python -m src.eda",
    "python -m src.feature_engineering",
    "python -m src.train_model",
    "python -m src.forecast",
    "python -m src.evaluate_model"
]

print("=" * 60)
print(" RETAIL SALES FORECASTING PIPELINE ")
print("=" * 60)

for step in steps:
    print(f"\nRunning: {step}")
    result = subprocess.run(step, shell=True)

    if result.returncode != 0:
        print(f"Error while executing: {step}")
        break

print("\nPipeline completed.")