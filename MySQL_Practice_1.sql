create database flipkart;
use flipkart;

-- Products - pid, pname, price, stock, location (Mumbai or Delhi)
create table products
(
	pid int(3) primary key,
    pname varchar(50) not null,
    price int(10) not null,
    stock int(5),
    location varchar(30) check(location in ('Mumbai','Delhi')));

-- Customer - cid, cname, age, addr
create table customer
(
	cid int(3) primary key,
    cname varchar(30) not null,
    age int(3), 
    addr varchar(50)
);

-- Orders - oid, cid, pid, amt
create table orders
(
	oid int(3) primary key,
    cid int(3),
    pid int(3),
    amt int(10) not null,
    foreign key(cid) references customer(cid),
    foreign key(pid) references products(pid));
    
   -- Payment - pay_id, oid,amount, mode(upi, cerdit, debit), status
create table payment
(
	pay_id int(3) primary key,
    oid int(3),
    amount int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit')),
    status varchar(30),
    foreign key(oid) references orders(oid)
);
 
 #Inserting values into products table
insert into products values(1,'HP Laptop',50000,15,'Mumbai');
insert into products values(2,'Realme Mobile',20000,30,'Delhi');
insert into products values(3,'Boat earpods',3000,50,'Delhi');
insert into products values(4,'Levono Laptop',40000,15,'Mumbai');
insert into products values(5,'Charger',1000,0,'Mumbai');
insert into products values(6, 'Mac Book', 78000, 6, 'Delhi');
insert into products values(7, 'JBL speaker', 6000, 2, 'Delhi');

#Inserting values into customer table
insert into customer (cid, cname, age, addr) values
(101,'Ravi',30,'abc'),
(102,'Rahul',25,'def'),
(103,'Simran',32,'jhi'),
(104,'Purvesh',28,'klm'),
(105,'Sanjana',22,'nop');

#Inserting values into orders table
insert into orders values(10001,102,3,2700);
insert into orders values(10002,104,2,18000);
insert into orders values(10003,105,5,900);
insert into orders values(10004,101,1,46000);


#inserting values into payment table
insert into payment values(201,10001,2700,'upi','completed');
insert into payment values(202,10002,18000,'credit','completed');
insert into payment values(203,10003,900,'debit','in process');

select*  from payment;

-- to delete table we use drop 
drop table payment ;

-- to drop whole database we use command
drop database flipkart;

-- from alter command we can add and modify the tables 
-- to add column in a table 
alter table customer
add phone varchar(10);

-- to delete a column 
alter table customer
drop column phone;

-- to modify datatype or add conditions
alter table products
modify column price varchar(10) ;

-- TURNCATE
-- The TRUNCATE TABLE command deletes the data inside a table, but not the table itself.
truncate table products ;

select * from products;
select * from customer;
select * from orders;
select * from payment;

-- Operators

-- Arithmetic Operators:
-- 1)
SELECT SUM(price) AS total_revenue 
FROM products;
-- 2)
SELECT * 
FROM products 
WHERE price % 3 = 0;
-- 3)
SELECT pid, pname, price, 
(price - (SELECT AVG(price) FROM products)) AS price_difference 
FROM products;

-- Comparison Operators:
-- 1)
SELECT * 
FROM products 
WHERE price >= 50000;
-- 2)
SELECT * 
FROM customer 
WHERE age != 30;
-- 3) 

-- Logical Operators:
-- 1)
SELECT * 
FROM products 
WHERE location = 'Mumbai' 
AND stock > 10;
-- 2)
SELECT * 
FROM customer 
WHERE addr LIKE '%Mumbai%' 
OR 
(SELECT SUM(amt) 
FROM orders o 
WHERE o.cid = customer.cid) > 20000;
-- 3)
SELECT * 
FROM payment 
WHERE mode != 'upi' 
AND status = 'completed';

    