from lib.customer_repository import CustomerRepository
from lib.customer import Customer
from lib.receipt import Receipt
from datetime import date

"""
When we call CustomerRepository#all
We get a list of Customer objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = CustomerRepository(db_connection) # Create a new CustomerRepository

    customers = repository.all() # Get all customers

    # Assert on the results
    assert customers == [
        Customer(1, 'Daniel'),
        Customer(2, 'Alessandro'),
        Customer(3, 'Alfie'),
        Customer(4, 'Jess'),
        Customer(5, 'Adam'),
        Customer(6, 'Taha'),
        Customer(7, 'Valeria'),
        Customer(8, 'Johannes'),
    ]

"""
When we call CustomerRepository#find
We get a single Customer object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = CustomerRepository(db_connection)

    customer = repository.find(3)
    assert customer == Customer(3, 'Alfie')

"""
When we call CustomerRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = CustomerRepository(db_connection)

    repository.create(Customer(None, 'Efaz'))

    result = repository.all()
    assert result == [
        Customer(1, 'Daniel'),
        Customer(2, 'Alessandro'),
        Customer(3, 'Alfie'),
        Customer(4, 'Jess'),
        Customer(5, 'Adam'),
        Customer(6, 'Taha'),
        Customer(7, 'Valeria'),
        Customer(8, 'Johannes'),
        Customer(9, 'Efaz'),
    ]

"""
When we call CustomerRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = CustomerRepository(db_connection)
    repository.delete(3) # Apologies to Alfie

    result = repository.all()
    assert result == [
        Customer(1, 'Daniel'),
        Customer(2, 'Alessandro'),
        Customer(4, 'Jess'),
        Customer(5, 'Adam'),
        Customer(6, 'Taha'),
        Customer(7, 'Valeria'),
        Customer(8, 'Johannes'),
    ]

def test_find_customer_orders(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = CustomerRepository(db_connection)

    result = repository.get_receipts(1)
    assert result == [
        Receipt(order_id=1, customer_id=1, customer_name='Daniel', item_id=1, item_name='Pencil', item_quantity=3, unit_price=.35, placed_on=date(2024, 10, 11)),
        Receipt(order_id=2, customer_id=1, customer_name='Daniel', item_id=2, item_name='Pen', item_quantity=2, unit_price=2.45, placed_on=date(2024, 10, 11))
    ]