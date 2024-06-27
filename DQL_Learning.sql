use flipkart;
-- A) GROUP BY using HAVING
SELECT cname, COUNT(*) AS Number
FROM customer
GROUP BY cname
HAVING Number >= 1;

-- B) GROUP BY using CONCAT.
-- Group Concat is used in MySQL to get concatenated values of expressions with more than one result per column.
SELECT location, GROUP_CONCAT(DISTINCT pname) AS product_names
FROM products
GROUP BY location;

-- a query to find the total stock of products for each location
SELECT location, SUM(stock) AS total_stock 
FROM products 
GROUP BY location;

--  a query to find the average age of customers grouped by their location (based on the address).
SELECT SUBSTRING(addr, 1, 3) AS location, AVG(age) AS avg_age 
FROM customer 
GROUP BY location;

-- ORDER BY
-- A) ASCENDING
SELECT pid, pname, price
FROM products
ORDER BY price ASC;

-- B) DESCENDING
SELECT cid, cname, age
FROM customer
ORDER BY age DESC;

--  to retrieve all products ordered by their price in descending order.
SELECT * 
FROM products 
ORDER BY price DESC;

-- retrieve all customers ordered by their age in ascending order.
SELECT * 
FROM customer 
ORDER BY age ASC;

-- HAVING BY
-- A) Find the products with a stock level less than 10.
SELECT pid, pname, stock
FROM products
GROUP BY pid, pname, stock
HAVING stock < 10;

-- B) Find the locations where the total stock of products is greater than 50.
SELECT location, SUM(stock) AS total_stock
FROM products
GROUP BY location
HAVING SUM(stock) > 50;

-- the locations where the total stock of products is greater than 20
SELECT location, SUM(stock) AS total_stock 
FROM products 
GROUP BY location 
HAVING SUM(stock) > 20;

-- the customers who have placed orders with a total amount greater than 10000
SELECT c.cid, c.cname, SUM(o.amt) AS total_amount 
FROM customer c 
JOIN orders o ON c.cid = o.cid 
GROUP BY c.cid, c.cname 
HAVING SUM(o.amt) > 10000;

--  the products that have a stock level between 10 and 20 and are located in Mumbai.
SELECT p.pid, p.pname, p.stock 
FROM products p 
WHERE p.location = 'Mumbai' 
GROUP BY p.pid, p.pname, p.stock 
HAVING p.stock BETWEEN 10 AND 20;

-- DQL COMMANDS

-- DQL COMMANDS
-- 1) DQL stands for Data Query Language.

-- SELECT
-- Used to retrieve rows selected from one or more tables.
-- SELECT can be used in many ways
-- A) SELECT With DISTINCT Clause
-- The DISTINCT Clause after SELECT eliminates duplicate rows from the result set.
SELECT DISTINCT cname,addr FROM customer;

-- B) SELECT all columns(*)
SELECT * FROM orders;

-- C) SELECT by column name
SELECT oid FROM orders;

-- D) SELECT with LIKE(%)
-- Basically helps in searching using some syllables of the name
-- a) "Ra" anywhere
SELECT * FROM customer WHERE cname LIKE "%Ra%";

-- b) Begins With "Ra"
SELECT * FROM customer WHERE cname LIKE "Ra%";

-- a) Ends With "vi
SELECT * FROM customer WHERE cname LIKE "%vi";

-- E) SELECT with CASE or IF
-- a) CASE
SELECT cid,
	   cname,
       CASE WHEN cid > 102 THEN 'Pass' ELSE 'Fail' END AS 'Remark'
FROM customer;

-- b) IF
SELECT cid,
	   cname,
       IF(cid > 102, 'Pass', 'Fail')AS 'Remark'
FROM customer;

-- F) SELECT with a LIMIT Clause
SELECT * 
FROM customer
ORDER BY cid
LIMIT 2;

-- G) SELECT with WHERE
SELECT * FROM customer WHERE cname = "Ravi";


