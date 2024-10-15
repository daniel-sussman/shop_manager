-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;
DROP TABLE IF EXISTS customers;
DROP SEQUENCE IF EXISTS customers_id_seq;
DROP TABLE IF EXISTS items;
DROP SEQUENCE IF EXISTS items_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name varchar(255),
    unit_price numeric(10, 2),
    quantity_stocked int
);

-- Create the second table.
CREATE SEQUENCE IF NOT EXISTS customers_id_seq;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name varchar(255)
);

-- Create the join table.
CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    item_id int,
    customer_id int,
    item_quantity int,
    placed_on date,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fk_customer foreign key(customer_id) references customers(id) on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO items (name, unit_price, quantity_stocked) VALUES ('Pencil', .35, 43);
INSERT INTO items (name, unit_price, quantity_stocked) VALUES ('Pen', 2.45, 33);
INSERT INTO items (name, unit_price, quantity_stocked) VALUES ('Paper', .03, 177);
INSERT INTO items (name, unit_price, quantity_stocked) VALUES ('Eraser', .85, 22);
INSERT INTO items (name, unit_price, quantity_stocked) VALUES ('Marker', 4.95, 40);

INSERT INTO customers (name) VALUES ('Daniel');
INSERT INTO customers (name) VALUES ('Alessandro');
INSERT INTO customers (name) VALUES ('Alfie');
INSERT INTO customers (name) VALUES ('Jess');
INSERT INTO customers (name) VALUES ('Adam');
INSERT INTO customers (name) VALUES ('Taha');
INSERT INTO customers (name) VALUES ('Valeria');
INSERT INTO customers (name) VALUES ('Johannes');

INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (1, 1, 3, '2024-10-11');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (2, 1, 2, '2024-10-11');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (5, 2, 1, '2024-10-12');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (2, 3, 3, '2024-10-12');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (3, 4, 5, '2024-10-12');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (2, 5, 1, '2024-10-12');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (3, 5, 10, '2024-10-12');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (4, 6, 10, '2024-10-13');
INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (1, 3, 4, '2024-10-13');


