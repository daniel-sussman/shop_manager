class Order:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, item_id, customer_id, item_quantity, placed_on):
        self.id = id
        self.item_id = item_id
        self.customer_id = customer_id
        self.item_quantity = item_quantity
        self.placed_on = placed_on

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Order
    def __repr__(self):
        return f"Order({self.id}, {self.item_id}, {self.customer_id}, {self.item_quantity}, {self.placed_on})"