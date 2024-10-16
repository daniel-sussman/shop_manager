from lib.item import Item

class ItemRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all items
    def all(self):
        rows = self._connection.execute('SELECT * from items')
        return [Item(row["id"], row["name"], row["unit_price"], row["quantity_stocked"]) for row in rows]

    # Find a single item by their id
    def find(self, item_id):
        rows = self._connection.execute(
            'SELECT * from items WHERE id = %s', [item_id])
        row = rows[0]
        return Item(row["id"], row["name"], row["unit_price"], row["quantity_stocked"])

    # Create a new item
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, item):
        self._connection.execute('INSERT INTO items (name, unit_price, quantity_stocked) VALUES (%s, %s, %s)',
            [item.name, item.unit_price, item.quantity_stocked])
        return None

    # Delete an item by their id
    def delete(self, item_id):
        self._connection.execute(
            'DELETE FROM items WHERE id = %s', [item_id])
        return None

    def update_quantity_stocked(self, item_id, new_value):
        self._connection.execute(
            'UPDATE items SET quantity_stocked = %s WHERE items.id = %s', [new_value, item_id])