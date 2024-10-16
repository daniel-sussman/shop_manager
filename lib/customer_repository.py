from lib.customer import Customer
from lib.receipt import Receipt

class CustomerRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all customers
    def all(self):
        rows = self._connection.execute('SELECT * from customers')
        return [Customer(row["id"], row["name"]) for row in rows]

    # Find a single customer by their id
    def find(self, customer_id):
        rows = self._connection.execute(
            'SELECT * from customers WHERE id = %s', [customer_id])
        row = rows[0]
        return Customer(row["id"], row["name"])

    # Create a new customer
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, customer):
        result = self._connection.execute('INSERT INTO customers (name) VALUES (%s) RETURNING id', [customer.name])
        customer_id = result[0]['id']
        return Customer(customer_id, customer.name)

    # Delete an customer by their id
    def delete(self, customer_id):
        self._connection.execute(
            'DELETE FROM customers WHERE id = %s', [customer_id])
        return None

    def get_receipts(self, customer_id):
        rows = self._connection.execute(
            'SELECT orders.id AS order_id, customers.id AS customer_id, customers.name AS customer_name, items.id AS item_id, items.name AS item_name, orders.item_quantity, items.unit_price, orders.placed_on ' \
            'FROM customers ' \
            'JOIN orders ON orders.customer_id = customers.id ' \
            'JOIN items ON orders.item_id = items.id ' \
            'WHERE customers.id = %s', [customer_id])
        
        return [Receipt(row['order_id'], row['customer_id'], row['customer_name'], row['item_id'], row['item_name'], row['item_quantity'], row['unit_price'], row['placed_on'])
            for row in rows]