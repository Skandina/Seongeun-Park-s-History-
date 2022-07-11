USE warehouse;
SELECT * FROM products ORDER BY id ASC;
SELECT * FROM customers ORDER BY id ASC;
SELECT * FROM staff ORDER BY id ASC;
SELECT * FROM orders ORDER BY products_id ASC;

CREATE TABLE products ( 
id int PRIMARY KEY not null, 
products_name VARCHAR(20),
price int,
amount int, 
created_at DATE,
updated_at DATE 
);

INSERT INTO products VALUES 
(1, "wand", 10000, 3, "2022-02-16", "2022-02-16"), 
(2, "cloak", 5000, 3, "2022-01-13", "2022-02-16"),
(3, "stone", 100000, 1, "2020-08-22", "2022-02-16"),
(4, "sword", 200000, 1, "2020-07-13", "2021-01-13"),
(5, "opal necklace", 150000, 1, "2017-01-01", "2018-08-09"),
(6, "time turners", 100000, 1, "2015-12-12", "2016-05-22"),
(7, "horcruxes", 70000, 7, "2020-10-11", "2021-10-14"),
(8, "nimbus 2000", 2000, 10, "2013-05-03", "2021-12-15"),
(9, "firebolt", 8000, 8, "2022-01-01", "2022-01-01"),
(10, "snitch", 1000, 50, "2019-05-05", "2020-07-07");

SET SQL_SAFE_UPDATES = 0;

CREATE TABLE customers (
id INT PRIMARY KEY NOT NULL, 
first_name VARCHAR(20),
last_name VARCHAR(20),
street VARCHAR(40),
postal_code INT,
age INT,
created_at DATE,
updated_at DATE
);

INSERT INTO customers VALUES 
(1, "Fredrika", "Pettersson", "Simpnas 27", 76186, 25, "2022-01-15", "2022-02-19"),
(2, "Jolin", "Olsson", "Langgatan 18", 54700, 27, "2020-05-27", "2022-02-15"),
(3, "Mostafa", "Isakson", "angsgatan 26", 73060, 73, "2020-04-18", "2022-02-15"),
(4, "Meya", "Arvidsson", "Vikarna 70", 45070, 62, "2018-03-23", "2022-02-12"),
(5, "Mathias", "Stromberg", "Sandviken 44", 29062, 40, "2018-05-15", "2022-02-10"),
(6, "Edward", "Engstrom", "Gokst 55", 67158, 68, "2017-04-04", "2022-02-09"),
(7, "Yasmin", "Lingdren", "Orrespelsv 3", 92034, 64, "2017-03-01", "2022-02-07"),
(8, "Hilding", "Berglund", "Langgatan 90", 54070, 49, "2016-08-21", "2022-02-07"),
(9, "Aina", "Magnusson", "Figgeberg Gardeby 58",88041, 46, "2016-06-29", "2022-02-04"),
(10, "Emy", "Arvidsson", "Nittsjo Kvarngatu 7", 91045, 65, "2015-01-30", "2022-02-03");

CREATE TABLE staff (
id INT PRIMARY KEY NOT NULL,
first_name VARCHAR(40),
last_name VARCHAR(40),
employee_since DATE,
age INT,
CREATED_AT DATE,
UPDATED_AT DATE);

INSERT INTO staff VALUES 
(1, "Havanna", "Isaksson", "2017-09-09", 34, "2017-09-09", "2021-09-09"),
(2, "Joshua", "Karlsson", "2017-10-25", 40, "2019-10-09", "2021-09-09"),
(3, "Wilma", "Carlsson", "2018-03-10", 37, "2017-03-10", "2021-09-09"),
(4, "Casandra", "Gunnarsson", "2018-05-25", 28, "2020-05-25", "2021-09-15"),
(5, "Olof", "Henriksson", "2019-07-03", 35, "2021-07-03", "2021-09-15"),
(6, "Narin", "Mattsson", "2019-02-22", 43, "2019-02-22", "2021-09-15"),
(7, "Mathias", "Henriksson", "2020-10-01", 40, "2020-10-01", "2021-12-22"),
(8, "Carolina", "Ek", "2021-01-01", 44, "2021-01-01", "2021-10-01"),
(9, "Estrid", "Eliasson", "2022-02-10", 35, "2022-02-10", "2021-10-01"),
(10, "Andreas", "Mattsson", "2022-02-10", 55, "2022-02-10", "2021-10-01");

CREATE TABLE orders (
products_id INT NOT NULL, FOREIGN KEY (products_id) REFERENCES products (id),
customers_id INT NOT NULL, FOREIGN KEY (customers_id) REFERENCES customers (id),
staff_id INT NOT NULL, FOREIGN KEY (staff_id) REFERENCES staff (id),
created_at DATE,
updated_at DATE
);

INSERT INTO orders (products_id, customers_id, staff_id, created_at, updated_at)
VALUES (
(SELECT id FROM products WHERE products_name = "cloak"), 
(SELECT id FROM customers WHERE first_name = "Fredrika"),
(SELECT id FROM staff WHERE first_name = "Havanna" ), "2022-01-19", "2022-02-15"
);

INSERT INTO orders (products_id, customers_id, staff_id, created_at, updated_at)
VALUES (
(SELECT id FROM products WHERE products_name = "cloak"), 
(SELECT id FROM customers WHERE first_name = "Jolin"),
(SELECT id FROM staff WHERE first_name = "Joshua" ), "2022-01-19", "2022-02-15"
);

INSERT INTO orders (products_id, customers_id, staff_id, created_at, updated_at)
VALUES (
(SELECT id FROM products WHERE products_name = "cloak"), 
(SELECT id FROM customers WHERE first_name = "Fredrika"),
(SELECT id FROM staff WHERE first_name = "Havanna" ), "2022-01-19", "2022-02-15"
);

SELECT * FROM orders;

INSERT INTO orders (products_id, customers_id, staff_id, created_at, updated_at)
VALUES (
(SELECT id FROM products WHERE products_name = "stone"), 
(SELECT id FROM customers WHERE first_name = "Mostafa"),
(SELECT id FROM staff WHERE first_name = "Wilma" ), "2022-01-19", "2022-02-15"
),
(
(SELECT id FROM products WHERE products_name = "sword"), 
(SELECT id FROM customers WHERE first_name = "Meya"),
(SELECT id FROM staff WHERE first_name = "Casandra" ), "2022-01-19", "2022-02-15"
),
(
(SELECT id FROM products WHERE products_name = "opal necklace"), 
(SELECT id FROM customers WHERE first_name = "Mathias"),
(SELECT id FROM staff WHERE first_name = "Olof" ), "2022-01-19", "2022-02-15"
),
(
(SELECT id FROM products WHERE products_name = "time turners"), 
(SELECT id FROM customers WHERE first_name = "Edward"),
(SELECT id FROM staff WHERE first_name = "Narin" ), "2022-01-19", "2022-02-15"
),
(
(SELECT id FROM products WHERE products_name = "horcruxes"), 
(SELECT id FROM customers WHERE first_name = "Yasmin"),
(SELECT id FROM staff WHERE first_name = "Mathias" ), "2022-01-19", "2022-02-15"
),
(
(SELECT id FROM products WHERE products_name = "nimbus 2000"), 
(SELECT id FROM customers WHERE first_name = "Hilding"),
(SELECT id FROM staff WHERE first_name = "Carolina" ), "2022-01-19", "2022-02-15"
),
(
(SELECT id FROM products WHERE products_name = "firebolt"), 
(SELECT id FROM customers WHERE first_name = "Aina"),
(SELECT id FROM staff WHERE first_name = "Estrid" ), "2022-01-19", "2022-02-15"
),
(
(SELECT id FROM products WHERE products_name = "snitch"), 
(SELECT id FROM customers WHERE first_name = "Emy"),
(SELECT id FROM staff WHERE first_name = "Andreas" ), "2022-01-19", "2022-02-15"
);

