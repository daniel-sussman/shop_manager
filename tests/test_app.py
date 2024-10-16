from app import Application
from data.string_resources import *
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
from unittest.mock import Mock

def initialize_tests(connection):
    connection.seed("seeds/shop_manager.sql")
    io = TerminalInterfaceHelperMock()
    app = Application(io, connection)
    return [io, app]

def boot_the_program(io):
    io.expect_print(WELCOME)
    io.expect_print(CUSTOMER_TYPE)

def exit_the_program(io, options=CUSTOMER_OPTIONS):
    io.expect_print(options)
    io.provide("q")

def create_new_customer(io):
    io.provide("n")
    io.expect_print(PROMPT_NAME)
    io.provide("Patrick")
    customer = Mock(id=9)
    customer.name = "Patrick"
    io.expect_print(ACCOUNT_CREATED(customer))

def login_as_returning_customer(io):
    io.provide("r")
    io.expect_print(PROMPT_ID)
    io.provide("1")
    io.expect_print(WELCOME_BACK("Daniel"))

def login_as_admin(io):
    io.provide("admin")
    io.expect_print(WELCOME_ADMIN)

def list_all_shop_items(io, options=CUSTOMER_OPTIONS):
    io.expect_print(options)
    io.provide("1")
    io.expect_print(LIST_ITEMS)
    qty = ['', '', '', '', ''] if options == CUSTOMER_OPTIONS else [f"{f'{n} in stock':>16}" for n in (43, 33, 177, 22, 40)]
    io.expect_print(f"  1 - Pencil.............. £0.35{qty[0]}\n  2 - Pen................. £2.45{qty[1]}\n  3 - Paper............... £0.03{qty[2]}\n  4 - Eraser.............. £0.85{qty[3]}\n  5 - Marker.............. £4.95{qty[4]}\n")

def list_customer_orders(io):
    io.expect_print(CUSTOMER_OPTIONS)
    io.provide("2")
    io.expect_print(LIST_ORDERS)
    io.expect_print("  order # |   placed on    | item # |  description   |  qty @ unit price  |    total\n ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n     1    |  11 Oct 2024   |   1    |     Pencil     |     3 @ £0.35      |    £1.05\n     2    |  11 Oct 2024   |   2    |      Pen       |     2 @ £2.45      |    £4.90\n")

def place_new_order(io):
    io.expect_print(CUSTOMER_OPTIONS)
    io.provide("3")
    io.expect_print(LIST_ITEMS)
    io.expect_print("  1 - Pencil.............. £0.35\n  2 - Pen................. £2.45\n  3 - Paper............... £0.03\n  4 - Eraser.............. £0.85\n  5 - Marker.............. £4.95\n")
    io.expect_print(PROMPT_ORDER_ITEM)
    io.provide("5")
    io.expect_print(PROMPT_ORDER_QTY(40))
    io.provide("2")
    io.expect_print(ORDER_CONFIRMATION(9.9))

def order_too_much(io):
    io.expect_print(CUSTOMER_OPTIONS)
    io.provide("3")
    io.expect_print(LIST_ITEMS)
    io.expect_print("  1 - Pencil.............. £0.35\n  2 - Pen................. £2.45\n  3 - Paper............... £0.03\n  4 - Eraser.............. £0.85\n  5 - Marker.............. £4.95\n")
    io.expect_print(PROMPT_ORDER_ITEM)
    io.provide("5")
    io.expect_print(PROMPT_ORDER_QTY(40))
    io.provide("41")
    io.expect_print(ORDER_UNSUCCESSFUL)

def add_new_item(io):
    io.expect_print(ADMIN_OPTIONS)
    io.provide("2")
    io.expect_print(PROMPT_NEW_ITEM_DESCRIPTION)
    io.provide("Writing pad")
    io.expect_print(PROMPT_NEW_ITEM_UNIT_PRICE)
    io.provide("3.50")
    io.expect_print(PROMPT_NEW_ITEM_QUANTITY)
    io.provide("20")
    io.expect_print(ITEM_ADDED_TO_SHOP)

def restock_item(io):
    io.expect_print(ADMIN_OPTIONS)
    io.provide("3")
    io.expect_print(LIST_ITEMS)
    io.expect_print("  1 - Pencil.............. £0.35     43 in stock\n  2 - Pen................. £2.45     33 in stock\n  3 - Paper............... £0.03    177 in stock\n  4 - Eraser.............. £0.85     22 in stock\n  5 - Marker.............. £4.95     40 in stock\n")
    io.expect_print(PROMPT_RESTOCK_ITEM)
    io.provide("1")
    io.expect_print(PROMPT_NEW_ITEM_QUANTITY)
    io.provide("100")
    io.expect_print(RESTOCK_CONFIRMATION)

def list_customers(io):
    io.expect_print(ADMIN_OPTIONS)
    io.provide("4")
    io.expect_print(LIST_CUSTOMERS)
    io.expect_print("  1 - Daniel\n  2 - Alessandro\n  3 - Alfie\n  4 - Jess\n  5 - Adam\n  6 - Taha\n  7 - Valeria\n  8 - Johannes\n")

def list_orders(io):
    io.expect_print(ADMIN_OPTIONS)
    io.provide("5")
    io.expect_print(LIST_ORDERS_ADMIN)
    io.expect_print(RECEIPT_HEADER_3 + '\n' + RECEIPT_HEADER_4 + "\n" \
        "     1    |   Daniel   |  11 Oct 2024   |   1    |     Pencil     |     3 @ £0.35      |    £1.05\n" \
        "     2    |   Daniel   |  11 Oct 2024   |   2    |      Pen       |     2 @ £2.45      |    £4.90\n" \
        "     3    | Alessandro |  12 Oct 2024   |   5    |     Marker     |     1 @ £4.95      |    £4.95\n" \
        "     4    |   Alfie    |  12 Oct 2024   |   2    |      Pen       |     3 @ £2.45      |    £7.35\n" \
        "     5    |    Jess    |  12 Oct 2024   |   3    |     Paper      |     5 @ £0.03      |    £0.15\n" \
        "     6    |    Adam    |  12 Oct 2024   |   2    |      Pen       |     1 @ £2.45      |    £2.45\n" \
        "     7    |    Adam    |  12 Oct 2024   |   3    |     Paper      |    10 @ £0.03      |    £0.30\n" \
        "     8    |    Taha    |  13 Oct 2024   |   4    |     Eraser     |    10 @ £0.85      |    £8.50\n" \
        "     9    |   Alfie    |  13 Oct 2024   |   1    |     Pencil     |     4 @ £0.35      |    £1.40\n"
    )

def list_orders_by_customer(io):
    io.expect_print(ADMIN_OPTIONS)
    io.provide("6")
    io.expect_print(LIST_CUSTOMERS)
    io.expect_print(PROMPT_CUSTOMER_ID)
    io.provide("3")
    io.expect_print(RECEIPT_HEADER_3 + '\n' + RECEIPT_HEADER_4 + "\n" \
        "     4    |   Alfie    |  12 Oct 2024   |   2    |      Pen       |     3 @ £2.45      |    £7.35\n" \
        "     9    |   Alfie    |  13 Oct 2024   |   1    |     Pencil     |     4 @ £0.35      |    £1.40\n"
    )

def delete_customer_account(io):
    io.expect_print(CUSTOMER_OPTIONS)
    io.provide("4")
    io.expect_print(ACCOUNT_DELETE_WARNING)
    io.provide("y")
    io.expect_print(ACCOUNT_DELETED("Daniel"))

def test_new_customer(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    create_new_customer(io)
    list_all_shop_items(io)
    exit_the_program(io)
    app.run()

def test_returning_customer(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_returning_customer(io)
    exit_the_program(io)
    app.run()
    
def test_list_all_shop_items(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_returning_customer(io)
    list_all_shop_items(io)
    exit_the_program(io)
    app.run()

def test_list_customer_orders(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_returning_customer(io)
    list_customer_orders(io)
    exit_the_program(io)
    app.run()

def test_create_new_order(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_returning_customer(io)
    place_new_order(io)
    exit_the_program(io)
    app.run()

def test_try_to_order_too_much(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_returning_customer(io)
    order_too_much(io)
    exit_the_program(io)
    app.run()

def test_delete_customer_account(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_returning_customer(io)
    delete_customer_account(io)
    app.run()

def test_login_as_admin(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_admin(io)
    exit_the_program(io, ADMIN_OPTIONS)
    app.run()

def test_list_items_as_admin(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_admin(io)
    list_all_shop_items(io, ADMIN_OPTIONS)
    exit_the_program(io, ADMIN_OPTIONS)
    app.run()

def test_add_new_item(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_admin(io)
    add_new_item(io)
    exit_the_program(io, ADMIN_OPTIONS)
    app.run()

def test_restock_an_item(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_admin(io)
    restock_item(io)
    exit_the_program(io, ADMIN_OPTIONS)
    app.run()

def test_show_all_customers(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_admin(io)
    list_customers(io)
    exit_the_program(io, ADMIN_OPTIONS)
    app.run()

def test_show_all_orders(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_admin(io)
    list_orders(io)
    exit_the_program(io, ADMIN_OPTIONS)
    app.run()

def test_get_orders_by_customer(db_connection):
    io, app = initialize_tests(db_connection)
    boot_the_program(io)
    login_as_admin(io)
    list_orders_by_customer(io)
    exit_the_program(io, ADMIN_OPTIONS)
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
