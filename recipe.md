# Two Tables (Many-to-Many) Design Recipe Template

_Copy this recipe template to design and create two related database tables having a Many-to-Many relationship._

## 1. Extract nouns from the user stories or specification

```
As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.
```

```
Nouns:

item, name, unit price, quantity, order, customer, name, quantity ordered, date of order
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| items                 | name, unit_price, quantity_stocked
| customer              | name
| order                 | item_id, customer_id, item_quantity, placed_on

1. Name of the first table (always plural): `items` 

    Column names: `name`, `unit_price`, `quantity_stocked`

2. Name of the second table (always plural): `customers` 

    Column names: `name`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: items
id: SERIAL
name: varchar(255)
unit_price: numeric(8, 2)
quantity_stocked: int

Table: customers
id: SERIAL
name: varchar(255)
```

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

```
1. Can one customer have many items? YES
2. Can one item have many customers? YES
```

_If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case._

## 5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `table1_table2`.

```
Join table for tables: items and customers
Join table name: orders
Columns: item_id, customer_id, item_quantity, placed_on
```

## 6. Write the SQL.

```sql
-- EXAMPLE
-- file: shop_manager.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name varchar(255),
  unit_price numeric(10, 2),
  quantity_stocked int
);

-- Create the second table.
CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name varchar(255)
);

-- Create the join table.
CREATE TABLE orders (
  item_id int,
  customer_id int,
  item_quantity int,
  placed_on date,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_customer foreign key(customer_id) references customers(id) on delete cascade,
  PRIMARY KEY (item_id, customer_id)
);

```

## 7. Create the tables.

```bash
psql -h 127.0.0.1 shop_manager < shop_manager.sql
```