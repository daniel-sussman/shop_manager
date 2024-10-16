class Receipt:
    def __init__(self, order_id, customer_id, customer_name, item_id, item_name, item_quantity, unit_price, placed_on, include_customer_name=False):
        self.order_id = order_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.item_id = item_id
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.unit_price = float(unit_price)
        self.placed_on = placed_on
        self.include_customer_name = include_customer_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        if self.include_customer_name:
            return f"  {self.order_id:^8}|{self.customer_name:^12}|{self.placed_on.strftime('%d %b %Y'):^16}|{self.item_id:^8}|{self.item_name:^16}|{self.item_quantity:>6} @ £{self.unit_price:<10}|{f'£{(self.item_quantity * self.unit_price):.2f}':>9}"
        else:
            return f"  {self.order_id:^8}|{self.placed_on.strftime('%d %b %Y'):^16}|{self.item_id:^8}|{self.item_name:^16}|{self.item_quantity:>6} @ £{self.unit_price:<10}|{f'£{(self.item_quantity * self.unit_price):.2f}':>9}"