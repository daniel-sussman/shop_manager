from lib.order_repository import OrderRepository
from lib.order import Order
from lib.item_repository import ItemRepository
from datetime import date

"""
When we call OrderRepository#all
We get a list of Order objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection) # Create a new OrderRepository

    orders = repository.all() # Get all orders

    # Assert on the results
    assert orders == [
        Order(1, 1, 1, 3, date(2024, 10, 11)),
        Order(2, 2, 1, 2, date(2024, 10, 11)),
        Order(3, 5, 2, 1, date(2024, 10, 12)),
        Order(4, 2, 3, 3, date(2024, 10, 12)),
        Order(5, 3, 4, 5, date(2024, 10, 12)),
        Order(6, 2, 5, 1, date(2024, 10, 12)),
        Order(7, 3, 5, 10, date(2024, 10, 12)),
        Order(8, 4, 6, 10, date(2024, 10, 13)),
        Order(9, 1, 3, 4, date(2024, 10, 13)),
    ]

"""
When we call OrderRepository#find
We get a single Order object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    order = repository.find(3)
    assert order == Order(3, 5, 2, 1, date(2024, 10, 12))

"""
When we call OrderRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    repository.create(Order(None, 4, 3, 17, date(2024, 10, 15)))

    result = repository.all()
    assert result == [
        Order(1, 1, 1, 3, date(2024, 10, 11)),
        Order(2, 2, 1, 2, date(2024, 10, 11)),
        Order(3, 5, 2, 1, date(2024, 10, 12)),
        Order(4, 2, 3, 3, date(2024, 10, 12)),
        Order(5, 3, 4, 5, date(2024, 10, 12)),
        Order(6, 2, 5, 1, date(2024, 10, 12)),
        Order(7, 3, 5, 10, date(2024, 10, 12)),
        Order(8, 4, 6, 10, date(2024, 10, 13)),
        Order(9, 1, 3, 4, date(2024, 10, 13)),
        Order(10, 4, 3, 17, date(2024, 10, 15)),
    ]

"""
When we call OrderRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Order(1, 1, 1, 3, date(2024, 10, 11)),
        Order(2, 2, 1, 2, date(2024, 10, 11)),
        Order(4, 2, 3, 3, date(2024, 10, 12)),
        Order(5, 3, 4, 5, date(2024, 10, 12)),
        Order(6, 2, 5, 1, date(2024, 10, 12)),
        Order(7, 3, 5, 10, date(2024, 10, 12)),
        Order(8, 4, 6, 10, date(2024, 10, 13)),
        Order(9, 1, 3, 4, date(2024, 10, 13)),
    ]

def test_ordering_an_item_removes_it_from_stock(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    order_repository = OrderRepository(db_connection)
    item_repository = ItemRepository(db_connection)

    item_id = 4
    initial_qty = item_repository.find(item_id).quantity_stocked
    qty_ordered = 17
    order_repository.create(Order(None, item_id, 3, qty_ordered, date(2024, 10, 15)))
    final_qty = item_repository.find(item_id).quantity_stocked
    assert final_qty == initial_qty - qty_ordered