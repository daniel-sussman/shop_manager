from lib.customer import Customer

"""
Customer constructs with an id and name
"""
def test_customer_constructs():
    customer = Customer(1, "Test Customer")
    assert customer.id == 1
    assert customer.name == "Test Customer"

"""
We can format customers to strings nicely
"""
def test_customers_format_nicely():
    customer = Customer(1, "Test Customer")
    assert str(customer) == "Customer(1, Test Customer)"
    # Try commenting out the `__repr__` method in lib/customer.py
    # And see what happens when you run this test again.

"""
We can compare two identical customers
And have them be equal
"""
def test_customers_are_equal():
    customer1 = Customer(1, "Test Customer")
    customer2 = Customer(1, "Test Customer")
    assert customer1 == customer2
    # Try commenting out the `__eq__` method in lib/customer.py
    # And see what happens when you run this test again.
