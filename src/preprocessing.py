import pandas as pd
from src.db_connection import get_connection, close_connection


def preprocess_data():
    conn = get_connection()

    if conn is None:
        return

    # Read data from MySQL
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)

    print("\nOriginal Shape:", df.shape)

    # -------------------------------
    # Handle Missing Values
    # -------------------------------
    df.dropna(inplace=True)

    # -------------------------------
    # Remove Duplicates
    # -------------------------------
    df.drop_duplicates(inplace=True)

    # -------------------------------
    # Convert Data Types
    # -------------------------------
    df["sale_date"] = pd.to_datetime(df["sale_date"])

    numeric_columns = [
        "price",
        "quantity",
        "discount",
        "sales"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col])

    print("Cleaned Shape:", df.shape)

    # -------------------------------
    # Save Clean Data
    # -------------------------------
    df.to_csv("outputs/cleaned_sales.csv", index=False)

    print("\n✅ Cleaned dataset saved to outputs/cleaned_sales.csv")

    close_connection(conn)

    return df


if __name__ == "__main__":
    preprocess_data()