from lib.item_repository import ItemRepository
from lib.item import Item

"""
When we call ItemRepository#all
We get a list of Item objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection) # Create a new ItemRepository

    items = repository.all() # Get all items

    # Assert on the results
    assert items == [
        Item(1, 'Pencil', .35, 43),
        Item(2, 'Pen', 2.45, 33),
        Item(3, 'Paper', .03, 177),
        Item(4, 'Eraser', .85, 22),
        Item(5, 'Marker', 4.95, 40),
    ]

"""
When we call ItemRepository#find
We get a single Item object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(3)
    assert item == Item(3, 'Paper', .03, 177)

"""
When we call ItemRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    repository.create(Item(None, 'Compass', 6.85, 8))

    result = repository.all()
    assert result == [
        Item(1, 'Pencil', .35, 43),
        Item(2, 'Pen', 2.45, 33),
        Item(3, 'Paper', .03, 177),
        Item(4, 'Eraser', .85, 22),
        Item(5, 'Marker', 4.95, 40),
        Item(6, 'Compass', 6.85, 8),
    ]

"""
When we call ItemRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Item(1, 'Pencil', .35, 43),
        Item(2, 'Pen', 2.45, 33),
        Item(4, 'Eraser', .85, 22),
        Item(5, 'Marker', 4.95, 40),
    ]

def test_update_item_quantity(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    repository.update_quantity_stocked(5, 50)
    
    result = repository.all()
    assert result == [
        Item(1, 'Pencil', .35, 43),
        Item(2, 'Pen', 2.45, 33),
        Item(3, 'Paper', .03, 177),
        Item(4, 'Eraser', .85, 22),
        Item(5, 'Marker', 4.95, 50),
    ]