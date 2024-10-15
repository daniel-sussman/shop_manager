class Receipt:
    def __init__(self, order_id, customer_id, item_id, item_name, item_quantity, unit_price, placed_on):
        self.order_id = order_id
        self.customer_id = customer_id
        self.item_id = item_id
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.unit_price = float(unit_price)
        self.placed_on = placed_on

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Order #{self.order_id}, placed on {self.placed_on.strftime('%d %b %Y')} -- Item #{self.item_id} {self.item_name}, {self.item_quantity} @ £{self.unit_price}/unit, Total price: £{(self.item_quantity * self.unit_price):.2f}"