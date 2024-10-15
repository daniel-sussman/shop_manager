from lib.order import Order

class OrderRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all orders
    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        return [Order(row["id"], row["item_id"], row["customer_id"], row["item_quantity"], row["placed_on"]) for row in rows]

    # Find a single order by their id
    def find(self, order_id):
        rows = self._connection.execute(
            'SELECT * from orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row["id"], row["item_id"], row["customer_id"], row["item_quantity"], row["placed_on"])

    # Create a new order
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, order):
        self._connection.execute('INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (%s, %s, %s, %s)',
            [order.item_id, order.customer_id, order.item_quantity, order.placed_on])
        return None

    # Delete an order by their id
    def delete(self, order_id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [order_id])
        return None
