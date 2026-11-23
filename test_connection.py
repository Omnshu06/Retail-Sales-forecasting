from src.db_connection import get_connection, close_connection

conn = get_connection()

if conn:
    print("Database connection successful!")
    close_connection(conn)