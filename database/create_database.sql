-- Create Database
CREATE DATABASE IF NOT EXISTS retail_sales_db;

USE retail_sales_db;

-- Create Sales Table
CREATE TABLE IF NOT EXISTS sales (

    transaction_id INT PRIMARY KEY,

    sale_date DATE,

    store_id INT,

    product_id INT,

    category VARCHAR(100),

    region VARCHAR(100),

    price DECIMAL(10,2),

    quantity INT,

    discount DECIMAL(5,2),

    sales DECIMAL(10,2)

);