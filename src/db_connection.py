import mysql.connector
from mysql.connector import Error


def get_connection():
    """
    Establishes a connection to the MySQL database.
    Update the password below with your MySQL root password.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Omnshu@123",   # <-- Change this
            database="retail_sales_db"
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Database")
            return connection

    except Error as e:
        print(f"❌ Database Connection Error: {e}")
        return None


def close_connection(connection):
    """
    Closes the database connection.
    """

    if connection is not None and connection.is_connected():
        connection.close()
        print("🔒 Database Connection Closed")