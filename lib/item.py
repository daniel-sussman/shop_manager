class Item:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, unit_price, quantity_stocked):
        self.id = id
        self.name = name
        self.unit_price = float(unit_price)
        self.quantity_stocked = quantity_stocked

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Item
    def __repr__(self):
        return f"Item({self.id}, {self.name}, {self.unit_price:.2f}, {self.quantity_stocked})"