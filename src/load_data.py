import pandas as pd
from src.db_connection import get_connection, close_connection


def load_csv_to_mysql(csv_path):
    """
    Load retail sales CSV into MySQL.
    """

    df = pd.read_csv(csv_path)

    # Convert date column
    df["sale_date"] = pd.to_datetime(df["sale_date"]).dt.date

    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    # Remove previous data
    cursor.execute("DELETE FROM sales")

    query = """
    INSERT INTO sales(
        transaction_id,
        sale_date,
        store_id,
        product_id,
        category,
        region,
        price,
        quantity,
        discount,
        sales
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    data = []

    for _, row in df.iterrows():
        data.append((
            int(row["transaction_id"]),
            row["sale_date"],
            int(row["store_id"]),
            int(row["product_id"]),
            row["category"],
            row["region"],
            float(row["price"]),
            int(row["quantity"]),
            float(row["discount"]),
            float(row["sales"])
        ))

    cursor.executemany(query, data)

    conn.commit()

    print(f"✅ {cursor.rowcount} records inserted successfully.")

    cursor.close()
    close_connection(conn)


if __name__ == "__main__":
    load_csv_to_mysql("data/retail_sales.csv")