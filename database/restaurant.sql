CREATE DATABASE IF NOT EXISTS restaurant_management;

USE restaurant_management;

-- ==========================================
-- RESET OLD TABLES
-- ==========================================

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS menu;

SET FOREIGN_KEY_CHECKS = 1;


-- ==========================================
-- MENU TABLE
-- ==========================================

CREATE TABLE menu (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    food_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL
);


-- ==========================================
-- FAST FOOD MENU
-- ==========================================

INSERT INTO menu (food_name, category, price)
VALUES
('Burger', 'Burger', 120),
('Cheese Burger', 'Burger', 150),
('Pizza', 'Pizza', 250),
('French Fries', 'Sides', 100),
('Veg Sandwich', 'Sandwich', 90),
('Cheese Sandwich', 'Sandwich', 130),
('Momos', 'Momos', 85),
('Spring Roll', 'Starters', 110),
('Pasta', 'Pasta', 180),
('Cold Drink', 'Beverage', 50);


-- ==========================================
-- CUSTOMER TABLE
-- ==========================================

CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) UNIQUE,
    table_number INT
);


-- ==========================================
-- 4 CUSTOMERS
-- ==========================================

INSERT INTO customer
(customer_name, phone_number, table_number)
VALUES
('Rahul Sharma', '9876543210', 1),
('Aman Verma', '9876543211', 2),
('Priya Singh', '9876543212', 3),
('Neha Gupta', '9876543213', 4);


-- ==========================================
-- ORDERS TABLE
-- ==========================================

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    food_id INT,
    quantity INT,
    total_price DECIMAL(10,2),
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id),

    FOREIGN KEY (food_id)
    REFERENCES menu(food_id)
);


-- ==========================================
-- CHECK DATA
-- ==========================================

SELECT * FROM menu;

SELECT * FROM customer;

SELECT * FROM orders;