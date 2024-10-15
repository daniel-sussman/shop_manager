from lib.item import Item

def test_item_constructs():
    item = Item(1, "Test Item", 3.50, 7)
    assert item.id == 1
    assert item.name == "Test Item"
    assert item.unit_price == 3.50
    assert item.quantity_stocked == 7

def test_items_format_nicely():
    item = Item(1, "Test Item", 3.50, 7)
    assert str(item) == "Item(1, Test Item, 3.50, 7)"
    # Try commenting out the `__repr__` method in lib/item.py
    # And see what happens when you run this test again.

"""
We can compare two identical items
And have them be equal
"""
def test_items_are_equal():
    item1 = Item(1, "Test Item", 3.50, 7)
    item2 = Item(1, "Test Item", 3.50, 7)
    assert item1 == item2
    # Try commenting out the `__eq__` method in lib/item.py
    # And see what happens when you run this test again.
