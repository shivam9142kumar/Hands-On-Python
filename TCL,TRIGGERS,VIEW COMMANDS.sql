use flipkart;

-- TCL (Transaction control language) Commands
/*
TCL commands are used to manage transactions, maintain ACID properties, and control the flow of data modifications.
TCL commands ensure the consistency and durability of data in a database. */

-- Commit: Saves a transaction to the database.

commit;

-- Rollback: Undoes a transaction or change that hasn't been saved to the database

rollback;

-- Savepoint: Temporarily saves a transaction for later rollback 

savepoint a;

-- here it will store that as a
-- after we can call that by rollback to a

rollback to a;

-- Triggers 

-- Trigger is a statement that a system executes automatically when there is any modification to the database

-- "SQL Trigger for Logging Product Insertions"
-- after insert
DELIMITER //
CREATE TRIGGER products_after_insert
AFTER INSERT ON products
FOR EACH ROW
BEGIN
  INSERT INTO product_log (pid, pname, price, stock, location, inserted_at)
  VALUES (NEW.pid, NEW.pname, NEW.price, NEW.stock, NEW.location, NOW());
END //
DELIMITER ;

-- create an SQL trigger to automatically update product stock levels after each new order is inserted into the 'orders' table?
DELIMITER //
CREATE TRIGGER orders_after_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE products
  SET stock = stock - 1
  WHERE pid = NEW.pid;
END //
DELIMITER ;

-- after update 

-- SQL trigger to log changes made to product information whenever an update occurs in the 'products' table?
DELIMITER //
CREATE TRIGGER products_after_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
  IF OLD.pid <> NEW.pid OR OLD.pname <> NEW.pname OR OLD.price <> NEW.price OR OLD.stock <> NEW.stock OR OLD.location <> NEW.location THEN
    INSERT INTO product_log (pid, pname, price, stock, location, updated_at)
    VALUES (OLD.pid, OLD.pname, OLD.price, OLD.stock, OLD.location, NOW());
  END IF;
END //
DELIMITER ;

-- after delete 

-- SQL trigger to prevent the deletion of a product from the 'products' table if there are existing orders referencing that product in the 'orders' table?
DELIMITER //
CREATE TRIGGER products_after_delete
AFTER DELETE ON products
FOR EACH ROW
BEGIN
  -- Log information about deleted product (optional)
  -- INSERT INTO product_log (pid, pname, price, stock, location, deleted_at)
  -- VALUES (OLD.pid, OLD.pname, OLD.price, OLD.stock, OLD.location, NOW());

  -- Check if there are existing orders referencing the deleted product
  DECLARE has_orders INT DEFAULT (0);

  SELECT COUNT(*) INTO has_orders
  FROM orders
  WHERE pid = OLD.pid;

  IF has_orders > 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete product with existing orders. Update or delete orders first.';
  END IF;
END //
DELIMITER ;

-- before insert

#Trigger for Automatic Payment Status on Payment Insert
DELIMITER //

CREATE TRIGGER set_default_payment_status
BEFORE INSERT ON payment
FOR EACH ROW
BEGIN
  IF NEW.status IS NULL THEN
    SET NEW.status = 'Pending';
  END IF;
END //

DELIMITER ;

-- 1.example creates or replaces a view named active_customers_mumbai that shows customer ID, name, and address for customers older than 25 who live in addresses containing "Mumbai"

CREATE OR REPLACE VIEW active_customers_mumbai AS
SELECT c.cid, c.cname, c.addr
FROM customer c
WHERE c.age > 25 AND c.addr LIKE '%Mumbai%';

-- 2. View for Customers and their Orders

create view CustomerOrders as
select c.cid, c.cname, o.oid, o.amt, p.pname
from customer c
join orders o on c.cid = o.cid
join products p on o.pid = p.pid;
	
-- 3.View for Total Orders by Location

create view TotalOrdersByLocation as
select p.location, p.pname, count(o.oid) as total_orders
from products p
join orders o on p.pid = o.pid
group by p.location, p.pname;

-- 4.View for Payment Status

create view OrderPaymentStatus as
select o.oid, o.amt, p.mode, p.status
from orders o
join payment p on o.oid = p.oid;

-- drop veiw 
-- removes a view from the database.
DROP VIEW active_customers_mumbai;


-- 2.Drop TotalOrdersByLocation View
drop view TotalOrdersByLocation;

-- Saving the command permently after running succesfully 

DELIMITER //
CREATE TRIGGER update_payment_status
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NEW.status = 'completed' THEN
        UPDATE payment
        SET status = 'completed'
        WHERE oid = NEW.oid;
    END IF;
END //
DELIMITER ;

-- Going to previous command 

DELIMITER //
CREATE TRIGGER check_stock_before_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE available_stock INT;
    SELECT stock INTO available_stock FROM products WHERE pid = NEW.pid;
    IF available_stock < NEW.amt THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient stock for this product';
    END IF;
END //
DELIMITER ;
