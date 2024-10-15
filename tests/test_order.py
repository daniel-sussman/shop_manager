from lib.order import Order
from datetime import date

def test_order_constructs():
    order = Order(1, 3, 2, 7, date(2024, 10, 15))
    assert order.id == 1
    assert order.item_id == 3
    assert order.customer_id == 2
    assert order.item_quantity == 7
    assert order.placed_on == date(2024, 10, 15)

def test_orders_format_nicely():
    order = Order(1, 3, 2, 7, date(2024, 10, 15))
    assert str(order) == "Order(1, 3, 2, 7, 2024-10-15)"
    # Try commenting out the `__repr__` method in lib/order.py
    # And see what happens when you run this test again.

"""
We can compare two identical orders
And have them be equal
"""
def test_orders_are_equal():
    order1 = Order(1, 3, 2, 7, date(2024, 10, 15))
    order2 = Order(1, 3, 2, 7, date(2024, 10, 15))
    assert order1 == order2
    # Try commenting out the `__eq__` method in lib/order.py
    # And see what happens when you run this test again.
