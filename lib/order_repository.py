from lib.order import Order
from lib.item_repository import ItemRepository
from lib.receipt import Receipt

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
        repository = ItemRepository(self._connection)
        item = repository.find(order.item_id)
        remaining_in_stock = item.quantity_stocked - order.item_quantity
        if remaining_in_stock < 0:
            return False
        
        self._connection.execute('INSERT INTO orders (item_id, customer_id, item_quantity, placed_on) VALUES (%s, %s, %s, %s)',
            [order.item_id, order.customer_id, order.item_quantity, order.placed_on])
        repository.update_quantity_stocked(order.item_id, remaining_in_stock)
        return True

    # Delete an order by their id
    def delete(self, order_id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [order_id])
        return None

    def get_receipts(self):
        rows = self._connection.execute(
            'SELECT orders.id AS order_id, customers.id AS customer_id, customers.name AS customer_name, items.id AS item_id, items.name AS item_name, orders.item_quantity, items.unit_price, orders.placed_on ' \
            'FROM customers ' \
            'JOIN orders ON orders.customer_id = customers.id ' \
            'JOIN items ON orders.item_id = items.id')
        
        return [Receipt(row['order_id'], row['customer_id'], row['customer_name'], row['item_id'], row['item_name'], row['item_quantity'], row['unit_price'], row['placed_on'], include_customer_name=True)
            for row in rows]