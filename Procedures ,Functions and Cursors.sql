use flipkart;

-- DELIMITER COMMAND: The DELIMITER command is used to change the standard delimiter(like a semicolon (;)), to a different character. 

-- PROCEDURES 
 /*  A procedure is a set of SQL statements that can be saved and reused.
  ~ Procedures can have input parameters (IN) and output parameters (OUT). */

-- EXAMPLE:
-- Procedure to select all products 

DELIMITER //
CREATE PROCEDURE select_all_products()
BEGIN
    SELECT * FROM products;
END //
DELIMITER ;

-- EXECUTING PROCEDURES
-- EXAMPLE:
-- Calling the select_all_products procedure
CALL select_all_products();


-- DROPPING PROCEDURES

DROP PROCEDURE select_all_products;

-- FUNCTIONS
/*
A function is a reusable block of code that performs a specific task and can return a value. */

-- EXAMPLE:
-- Function to calculate total revenue for a product
DELIMITER $$
CREATE FUNCTION get_total_revenue()
RETURNS INT
DETERMINISTIC 
BEGIN
DECLARE total_revenue INT; 
SELECT SUM(p.amount) INTO total_revenue
FROM payment p
INNER JOIN orders o ON p.oid = o.oid
WHERE p.status = 'completed';
RETURN total_revenue; -- Returns the calculated total revenue
END$$
DELIMITER ;

-- FUNCTION EXECUTION

SELECT get_total_revenue(); -- This will execute the function and return the total revenue

-- DROPPING FUNCTION

DROP FUNCTION IF EXISTS get_total_revenue; -- This will remove the 'get_total_revenue' function from the database

 -- Creating procedure with IN
DELIMITER //
CREATE PROCEDURE get_product_details(IN product_id INT)
BEGIN
    SELECT * FROM products WHERE pid = product_id;
END //

-- Calling Procedure
CALL get_product_details(1);

-- OUT

-- Create the procedure to get product count using OUT
DELIMITER //
CREATE PROCEDURE get_product_count(OUT product_count INT)
BEGIN
    SELECT COUNT(*) INTO product_count FROM products;
END //

-- Calling the OUT Procedure
CALL get_product_count(@product_count);
SELECT @product_count as product_count;

-- CURSOR

-- To calculate the number of customers
DELIMITER //
DECLARE @customer_count INT;

SELECT @customer_count = COUNT(*)
FROM customer;

PRINT 'Number of customers: ' + CAST(@customer_count AS VARCHAR(10));
DELIMITER ;

-- To calculate the sum of prices for all HP laptops
DELIMITER //
DECLARE @total_price INT;

SELECT @total_price = SUM(price)
FROM products
WHERE pname = 'HP Laptop';
PRINT 'Total price of all HP Laptops: ' + CAST(@total_price AS VARCHAR(20));
DELIMITER ;

-- calculates the total revenue from the 'orders' and 'payment' tables for completed orders, and call the function to get the total revenue.
DELIMITER $$
CREATE PROCEDURE select_all_products()
BEGIN
    SELECT * FROM products;
END$$
DELIMITER ;

CALL select_all_products();

-- create a procedure with an OUT parameter to get the count of products in the 'products' table, store it in a variable, 
-- and select the variable to display the count.

DELIMITER $$
CREATE PROCEDURE get_product_count(OUT total_count INT)
BEGIN
    SELECT COUNT(*) INTO total_count FROM products;
END$$
DELIMITER ;

CALL get_product_count(@count);
SELECT @count AS total_products;


-- Write a query to declare and use a cursor to iterate through the 'products' table and print the product name for each product.

DELIMITER //
CREATE PROCEDURE print_product_names()
BEGIN
    DECLARE product_name VARCHAR(100);
    DECLARE done INT DEFAULT FALSE;
    DECLARE product_cursor CURSOR FOR SELECT name FROM products;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN product_cursor;

    get_names: LOOP
        FETCH product_cursor INTO product_name;
        IF done THEN
            LEAVE get_names;
        END IF;
        SELECT product_name;
    END LOOP get_names;

    CLOSE product_cursor;
END;
DELIMITER ;