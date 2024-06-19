-- JOINS
-- The word suggests, Joins are used to combine two or more tables to get specific data/information.

-- 1.Inner Join -> Matching values from both tables should be present.
use flipkart;

-- Creating table employee - eid, ename, phone_no., department, manager_id
CREATE TABLE employee(
eid INT(4) PRIMARY KEY,
ename VARCHAR(40) NOT NULL,
phone_no INT(10) NOT NULL,
department VARCHAR(40) NOT NULL,
manager_id INT(4)
);

-- Inserting into employee table
INSERT INTO employee VALUES (401, "Rohan", 364832549, "Analysis", 404);
INSERT INTO employee VALUES (402, "Rahul", 782654123, "Delivery", 406);
INSERT INTO employee VALUES (403, "Shyam", 856471235, "Delivery", 402);
INSERT INTO employee VALUES (404, "Neha", 724863287, "Sales", 402);
INSERT INTO employee VALUES (405, "Sanjana", 125478954, "HR", 404);
INSERT INTO employee VALUES (406, "Sanjay", 956478535, "Tech",null);

select * from employee;

 -- For getting the name of customers who placed the order, we need to inner join customer and orders table

SELECT customer.cid, cname, orders.oid FROM orders 
INNER JOIN customer ON orders.cid = customer.cid;

-- now getting the name of the customers and products that were ordered, we need to inner join orders, products and customer table

SELECT customer.cid, cname, products.pid, pname, oid FROM orders
INNER JOIN products ON orders.pid = products.pid
INNER JOIN customer ON orders.cid = customer.cid;

-- Dispaly oid, amt, cname, payment mode of orders which were made by people below 30 years

SELECT orders.oid, cname, amt, mode FROM orders
INNER JOIN payment ON orders.oid = payment.oid
INNER JOIN customer ON orders.cid = customer.cid
WHERE age < 30;

-- Dispaly oid, amt, cname, paymentmode of orders which were made by people below 30 years and payment was made through "Credit"

SELECT orders.oid, cname, amt, mode FROM orders
INNER JOIN payment ON orders.oid = payment.oid
INNER JOIN customer ON orders.cid = customer.cid
WHERE age < 30 AND mode = "Credit";

-- We have order table, want to also display details of product ordered and details of customer who placed the order

SELECT orders.cid, cname, pname FROM orders
INNER JOIN customer ON orders.cid = customer.cid
INNER JOIN products ON orders.pid = products.pid;

-- 2. Left Outer Join-> All the rows from the left table should be present and matching rows from the right table are present

-- Getting the product id, product name, amount to be paid in an order, we need to left join products and orders table

SELECT products.pid, pname, amt, orders.oid FROM products
LEFT JOIN orders ON orders.pid = products.pid;

-- Display details of all orders which were delivered from "Mumbai"

SELECT * FROM orders 
LEFT JOIN products ON orders.pid = products.pid
WHERE location = "Mumbai";

-- 3. Right Join-> All the rows from the right table should be present and only matching rows from the left table are present 

-- Displaying order details in paymnets table, we need to right join payment and orders table

SELECT * FROM payment 
RIGHT JOIN orders ON orders.oid = payment.oid;

-- Display details of all orders which were delivered from "Mumbai"

SELECT * FROM orders 
LEFT JOIN products ON orders.pid = products.pid
WHERE location = "Mumbai";

-- 4.Full Join-> All the rows from both the table should be present 

-- Displaying the details of all the orders and products, we need to full join orders and products tables 

SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
LEFT JOIN products ON orders.pid = products.pid
UNION
SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
RIGHT JOIN products ON orders.pid = products.pid;

-- 5.Self Join-> It is a regular join, but the table is joined by itself
-- Displaying the employees with managers, we need to self join the employee table 

SELECT e1.ename AS Employee, e2.ename AS Manager FROM employee e1
INNER JOIN employee e2 ON e1.manager_id = e2.eid;

-- 6.Cross Join-> It is used to view all the possible combinations of the rows of one table and with all the rows from second table

-- Displaying all the details of customer and orders where amount is less than 3000, we need to cross join customer and orders table

SELECT customer.cid, cname, orders.oid, amt FROM customer
CROSS JOIN orders ON customer.cid = orders.cid
WHERE amt > 3000;

-- Display oid, amount, cname, pname, location of the orders whose payment is still pending or in process

SELECT orders.oid, cname, pname, amount, status, location FROM orders
CROSS JOIN products ON orders.pid = products.pid
CROSS JOIN customer ON orders.cid = customer.cid
CROSS JOIN payment ON orders.oid = payment.oid
WHERE status IN ("in process", "pending");