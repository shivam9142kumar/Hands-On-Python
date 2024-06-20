 use flipkart;

/*  Subqueries	:
		-Single row subqueries
		-Multi row subqueries
		-Correlated subqueries queries  */

/* The single-row subquery returns one row. Multiple-row subqueries return sets of rows. 
These queries are commonly used to generate result sets that will be passed to a DML or SELECT statement for further processing. 
Both single-row and multiple-row subqueries will be evaluated once, before the parent query is run. 
"Single-row and multiple-row subqueries can be used in the WHERE and HAVING clauses of the parent query." */


/*CORELATED SUBQUERIES: SQL Correlated Subqueries are used to select data from a table referenced in the outer query.*/

-- SINGLE ROW SUBQUERIES:-
-- Example 1:- Find the customer who placed the order with the highest amount

select cname from customer 
where cid=(select cid   
from orders 
order by amt 
desc limit 1);

-- Example 2: Find the product with the highest price

select pname from products 
where price=(select max(price) from products);

-- we can see that at the end these above quiuers only display 1 row which menas those are single row quieres 

-- MULTIPLE-ROW SUBQUERIES
-- Example 1: Find all customers who have placed an order

SELECT cname
FROM customer
WHERE cid IN (SELECT cid
FROM orders);

-- Example 2: Find all customers who have placed an order for a product from Mumbai

SELECT cname
FROM customer
WHERE cid IN (SELECT cid FROM orders
WHERE pid IN (SELECT pid FROM products WHERE location = 'Mumbai'));


-- CORRELATED SUBQUERIES

-- Example 1: Products with Price Higher than Location Average

SELECT pname, price
FROM products p
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE location = p.location );

-- Example 2: Customers with Orders Exceeding Average Order Amount

SELECT cname
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.cid = c.cid
    GROUP BY o.cid
    HAVING AVG(o.amt) > (
        SELECT AVG(amt)
        FROM orders
    )
);

-- Find the name of the customer who placed the order with the highest total amount

SELECT cname 
FROM customer 
WHERE cid = (
    SELECT cid 
    FROM orders 
    GROUP BY cid 
    ORDER BY SUM(amt) DESC 
    LIMIT 1
);

-- Retrieve the names of all customers who have placed orders for products located in the same city as the customer named "Rahul". 

SELECT cname
FROM customer
WHERE cid IN (
    SELECT DISTINCT cid
    FROM orders
    WHERE pid IN (
        SELECT pid
        FROM products
        WHERE location = (
            SELECT location
            FROM customer
            WHERE cname = 'Rahul'
        )
    )
);
-- JOINS

/* INNER JOIN with subquery :- SQL JOINS are used to combine more than two or more tables together to extract 
						the useful data from all the tables. In this article, we will discuss INNER JOIN in SQL. */

-- Example:-To retrieves the products with their corresponding orders where the product price is greater than 1000.

SELECT p.pname, o.oid, o.amt
FROM products p
INNER JOIN (
    SELECT *
    FROM orders
) o ON p.pid = o.pid
WHERE p.price > 1000;

/* 2. LEFT JOIN with aggregate functions-The LEFT JOIN keyword returns all records from the left table (table1), and the 
       matching records from the right table (table2). The result is 0 records from the right side, if there is no match. */

-- Example - To retrieves all products and their total orders' amounts, even if there are no orders.

SELECT p.pname, SUM(o.amt) AS total_orders_amount
FROM products p
LEFT JOIN orders o ON p.pid = o.pid
GROUP BY p.pname;

--  Retrieve the names of customers who have placed orders for products with a price higher than the average price of all products in the same city as the customer,
--  and also display the total amount spent by each customer on such orders.

SELECT c.cname, SUM(o.amt) AS total_amount_spent
FROM customer c
INNER JOIN orders o ON c.cid = o.cid
INNER JOIN products p ON o.pid = p.pid
INNER JOIN (
    SELECT location, AVG(price) AS avg_price
    FROM products
    GROUP BY location
) avg_prices ON p.location = avg_prices.location
WHERE p.price > avg_prices.avg_price
GROUP BY c.cname;

-- Retrieve the names of all customers along with the total amount they have spent on orders, including customers who have not placed any orders yet.

SELECT c.cname, COALESCE(SUM(o.amt), 0) AS total_amount_spent
FROM customer c
LEFT JOIN orders o ON c.cid = o.cid
GROUP BY c.cname;

-- Analytics functions / Advanced functions

-- 1. RANK : RANK() gives a 'rank' to each row within a partition, based on an ordered set. 
--              If rows have the same value, they get the same rank. 

-- Example- Display rank of products on the basis of price using RANK() FUNCTION.

SELECT pid, pname, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

-- Retrieve the names of products along with their prices and the ranking of each product based on their prices, 
-- where the products are ranked in descending order of price.

SELECT pname, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

-- 2. DENSE_RANK
-- DENSE_RANK() is similar to RANK(), but it does not create gaps when there are ties. 
-- Rows with the same value will get the same rank, but the next rank will be consecutive.

-- Example- Display rank of products on the basis of price using DENSE_RANK() FUNCTION 

SELECT pid, pname, price, 
	DENSE_RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

-- Retrieve the names of products along with their prices and the dense ranking of each product based on their prices,
-- where products are ranked in descending order of price.

SELECT pname, price, DENSE_RANK() OVER (ORDER BY price DESC) AS dense_price_rank
FROM products;

-- 3. ROW_NUMBER
-- ROW_NUMBER() assigns a unique row number to each record in a partitioned or ordered set. 
-- This always gives unique numbers, even if there are ties.

-- EXAMPLE- Find Unique Row number of the Customer table  using Row number Fuction.

SELECT ROW_NUMBER() OVER (ORDER BY age DESC) AS row_num, cid, cname, age, addr
FROM customer;

-- Retrieve the names of products along with their prices and the row number of each product,
-- where products are ordered by their prices in descending order.

SELECT pname, price, ROW_NUMBER() OVER (ORDER BY price DESC) AS row_num
FROM products;

 -- 4.CUME_DIST
--  It shows the relative position of a row within a data set, indicating what fraction of the data set is at or below a particular value.

-- Example:-Find Cumulative Distribution of payment done based on amount spend

SELECT oid, amount,
       CUME_DIST() OVER (ORDER BY amount) AS cumulative_distribution
FROM payment;

-- Retrieve the names of products along with their prices and the cumulative distribution of each product's price, 
-- indicating what fraction of products have prices less than or equal to the price of each product.

SELECT pname, price, CUME_DIST() OVER (ORDER BY price) AS cumulative_distribution
FROM products;

-- 5. LAG
-- The LAG() function provides access to a row at a specified physical offset prior to the current row within the partition.

-- EXAMPLE- FIND LAG OF PRICE FROM PRODUCTS TABLE

SELECT pname, price, location,LAG(price) OVER (PARTITION BY location ORDER BY price) AS lag_price
FROM products;

--  Retrieve the names of products along with their prices and the price of the previous product in the list, ordered by price in ascending order.

SELECT pname, price, LAG(price) OVER (ORDER BY price) AS previous_price
FROM products;

-- 4. LEAD
-- The LEAD() function provides access to a row at a specified physical offset after the current row within the partition.

-- EXAMPLE-FIND LEAD PRICE OF THE PRODUCTS FROM PRODUCTS TABLE.

SELECT pname, price, location,LEAD(price) OVER (PARTITION BY location ORDER BY price) AS lead_price
FROM products;

-- Retrieve the names of products along with their prices and the price of the next product in the list, ordered by price in ascending order.

SELECT pname, price, LEAD(price) OVER (ORDER BY price) AS next_price
FROM products;