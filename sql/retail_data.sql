-- Create tables

CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);

CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);

CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT);

CREATE TABLE order_items (id INTEGER PRIMARY KEY, order_id INTEGER, product_id INTEGER, quantity INTEGER);



-- Insert data

INSERT INTO customers (id, name) VALUES
(1, 'Fatima Usman'),
(2, 'John Obi'),
(3, 'Adaeze Okoro'),
(4, 'David Eze'),
(5, 'Amina Bello'),
(6, 'Tunde Bakare'),
(7, 'Ngozi Nwosu'),
(8, 'Chinedu Okafor'),
(9, 'Halima Ibrahim'),
(10, 'Ifeanyi Ubah');



INSERT INTO products (id, name, category, price) VALUES
(1, 'Laptop', 'Electronics', 350000),
(2, 'Smartphone', 'Electronics', 200000),
(3, 'Headphones', 'Electronics', 20000),
(4, 'Office Chair', 'Furniture', 45000),
(5, 'Table', 'Furniture', 60000),
(6, 'Notebook', 'Stationery', 1500),
(7, 'Pen', 'Stationery', 300),
(8, 'Pencil', 'Stationery', 200),
(9, 'Water Bottle', 'Home Essentials', 2500),
(10, 'Backpack', 'Accessories', 15000);



INSERT INTO orders (id, customer_id, order_date) VALUES
(1, 1, '2024-01-07'),
(2, 1, '2024-03-25'),
(3, 1, '2024-04-19'),
(4, 2, '2024-02-09'),
(5, 3, '2024-03-22'),
(6, 4, '2024-04-09'),
(7, 5, '2024-01-06'),
(8, 5, '2024-01-26'),
(9, 5, '2024-01-05'),
(10, 6, '2024-01-08'),
(11, 6, '2024-04-15'),
(12, 7, '2024-01-23'),
(13, 7, '2024-03-26'),
(14, 8, '2024-01-20'),
(15, 8, '2024-02-12'),
(16, 8, '2024-04-14'),
(17, 9, '2024-02-26'),
(18, 9, '2024-01-02'),
(19, 9, '2024-03-13'),
(20, 9, '2024-02-14'),
(21, 10, '2024-04-24');



INSERT INTO order_items (id, order_id, product_id, quantity) VALUES
(1, 1, 10, 1),
(2, 1, 1, 2),
(3, 1, 5, 3),
(4, 2, 6, 5),
(5, 3, 4, 5),
(6, 4, 1, 3),
(7, 4, 4, 5),
(8, 4, 10, 4),
(9, 5, 10, 2),
(10, 5, 5, 3),
(11, 5, 7, 3),
(12, 6, 5, 1),
(13, 6, 1, 1),
(14, 6, 7, 4),
(15, 7, 7, 3),
(16, 7, 3, 3),
(17, 7, 5, 5),
(18, 8, 4, 5),
(19, 8, 8, 5),
(20, 9, 7, 5),
(21, 10, 2, 2),
(22, 10, 7, 1),
(23, 11, 10, 2),
(24, 11, 2, 2),
(25, 12, 9, 5),
(26, 13, 1, 1),
(27, 13, 4, 1),
(28, 14, 9, 5),
(29, 15, 4, 3),
(30, 15, 1, 5),
(31, 15, 7, 2),
(32, 16, 7, 2),
(33, 16, 5, 5),
(34, 16, 6, 2),
(35, 17, 6, 5),
(36, 17, 2, 2),
(37, 17, 8, 4),
(38, 18, 10, 3),
(39, 18, 6, 4),
(40, 19, 9, 4),
(41, 20, 6, 1),
(42, 21, 3, 5),
(43, 21, 6, 4);

