from lib.receipt import Receipt
from datetime import date

def test_receipt_constructs():
    receipt = Receipt(order_id=1, customer_id=4, customer_name='Jess', item_id=5, item_name='Test item', item_quantity=3, unit_price=.35, placed_on=date(2024, 10, 11))
    assert receipt.order_id == 1
    assert receipt.customer_id == 4
    assert receipt.item_id == 5
    assert receipt.item_name == 'Test item'
    assert receipt.item_quantity == 3
    assert receipt.unit_price == .35
    assert receipt.placed_on == date(2024, 10, 11)

def test_receipts_format_nicely():
    receipt = Receipt(order_id=1, customer_id=4, customer_name='Jess', item_id=5, item_name='Test item', item_quantity=3, unit_price=.35, placed_on=date(2024, 10, 11))
    assert str(receipt) == "     1    |  11 Oct 2024   |   5    |   Test item    |     3 @ £0.35      |    £1.05"
"""
We can compare two identical receipts
And have them be equal
"""
def test_receipts_are_equal():
    receipt1 = Receipt(order_id=1, customer_id=4, customer_name='Jess', item_id=5, item_name='Test item', item_quantity=3, unit_price=.35, placed_on=date(2024, 10, 11))
    receipt2 = Receipt(order_id=1, customer_id=4, customer_name='Jess', item_id=5, item_name='Test item', item_quantity=3, unit_price=.35, placed_on=date(2024, 10, 11))
    assert receipt1 == receipt2
