from app import Application
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock

def test_new_customer_scenario(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    io = TerminalInterfaceHelperMock()
    app = Application(io, db_connection)
    io.expect_print("Welcome to the shop management program!")
    io.expect_print("Are you a new or a returning customer? (n/r)")
    io.provide("n")
    io.expect_print("What is your name?")
    io.provide("Patrick")
    io.expect_print("Patrick, your account has been created! Your ID number is 9.")
    io.expect_print("What would you like to do?\n  1 - List all shop items\n  2 - See your past orders\n  3 - Place a new order\n  4 - Delete my account\n  q - Exit")
    io.provide("1")
    io.expect_print("We stock the following items:")
    io.expect_print("  1 - Pencil.............. £0.35\n  2 - Pen................. £2.45\n  3 - Paper............... £0.03\n  4 - Eraser.............. £0.85\n  5 - Marker.............. £4.95\n")
    io.expect_print("What would you like to do?\n  1 - List all shop items\n  2 - See your past orders\n  3 - Place a new order\n  4 - Delete my account\n  q - Exit")
    io.provide("q")
    app.run()

def test_returning_customer_scenario(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    io = TerminalInterfaceHelperMock()
    app = Application(io, db_connection)
    io.expect_print("Welcome to the shop management program!")
    io.expect_print("Are you a new or a returning customer? (n/r)")
    io.provide("r")
    io.expect_print("Please log in with your customer id:")
    io.provide("1")
    io.expect_print("Welcome back, Daniel!")
    io.expect_print("What would you like to do?\n  1 - List all shop items\n  2 - See your past orders\n  3 - Place a new order\n  4 - Delete my account\n  q - Exit")
    io.provide("1")
    io.expect_print("We stock the following items:")
    io.expect_print("  1 - Pencil.............. £0.35\n  2 - Pen................. £2.45\n  3 - Paper............... £0.03\n  4 - Eraser.............. £0.85\n  5 - Marker.............. £4.95\n")
    io.expect_print("What would you like to do?\n  1 - List all shop items\n  2 - See your past orders\n  3 - Place a new order\n  4 - Delete my account\n  q - Exit")
    io.provide("4")
    io.expect_print("This will delete your account permanently! Are you sure you want to proceed? (y/n)")
    io.provide("y")
    io.expect_print("Your account was deleted. Goodbye forever, Daniel!")
    app.run()
    
# Welcome to the shop management program!

# What do you want to do?
#   1 = list all shop items
#   2 = create a new item
#   3 = list all orders
#   4 = create a new order

# 1 [enter]

# Here's a list of all shop items:

#  #1 Super Shark Vacuum Cleaner - Unit price: 99 - Quantity: 30
#  #2 Makerspresso Coffee Machine - Unit price: 69 - Quantity: 15
#  (...)
