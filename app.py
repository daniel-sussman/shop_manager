from data.string_resources import *
from lib.database_connection import DatabaseConnection
from lib.item import Item
from lib.customer import Customer
from lib.order import Order
from lib.item_repository import ItemRepository
from lib.customer_repository import CustomerRepository
from lib.order_repository import OrderRepository
from lib.receipt import Receipt

import sys
from datetime import date

class Admin:
    pass


class ExitProgram(Exception):
    pass


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)


class Application():
    def __init__(self, io, connection):
        self.io = io
        self.connection = connection
        self.user = None
        self._item_repository = ItemRepository(self.connection)
        self._customer_repository = CustomerRepository(self.connection)
        self._order_repository = OrderRepository(self.connection)

    def run(self):
        self._show(WELCOME)
        self.user = self._get_user()
        if type(self.user) == Customer:
            self._customer_interface()
        else:
            self._admin_interface()

    def _admin_interface(self):
        while True:
            try:
                response = self._prompt(ADMIN_OPTIONS)
                if response == "1":
                    self._list_all_items()
                elif response == "2":
                    self._add_item()
                elif response == "3":
                    self._restock_item()
                elif response == "4":
                    self._list_all_customers()
                elif response == "5":
                    self._list_all_orders()
                elif response == "6":
                    pass # view orders by customer
                else:
                    self._invalid_response()
            except ExitProgram:
                break
    
    def _customer_interface(self):
        while True:
            try:
                response = self._prompt(CUSTOMER_OPTIONS)
                if response == "1":
                    self._list_all_items()
                elif response == "2":
                    self._list_my_orders()
                elif response == "3":
                    self._place_new_order()
                elif response == "4":
                    self._delete_account()
                else:
                    self._invalid_response()
            except ExitProgram:
                break

    def _get_user(self):
        while True:
            response = self._prompt(CUSTOMER_TYPE).lower()

            if response == 'r':
                customer = self._prompt_for_id()
                if customer is not None:
                    return customer
            if response == 'n':
                return self._create_new_customer()
            if response == 'admin':
                return self._login_admin()
            
            self._invalid_response()

    def _create_new_customer(self):
        customer_name = self._prompt(PROMPT_NAME)
        customer = self._customer_repository.create(Customer(None, customer_name))
        self._show(ACCOUNT_CREATED(customer))
        return customer

    def _delete_account(self):
        response = self._prompt(ACCOUNT_DELETE_WARNING)
        if response.lower() == "y":
            self._show(ACCOUNT_DELETED(self.user.name))
            self._customer_repository.delete(self.user.id)
            raise ExitProgram

    def _prompt_for_id(self):
        customer_ids = [customer.id for customer in self._customer_repository.all()]
        response = self._prompt(PROMPT_ID, int)

        if response in customer_ids:
            customer = self._customer_repository.find(response)
            self._show(WELCOME_BACK(customer.name))
            return customer
        self._invalid_response()

    def _prompt_for_customer(self, customers):
        for customer in customers:
            self._show(f"  {customer.id} - {customer.name}")

        return self._prompt("Select a customer:")
    
    def _login_admin(self):
        self._show(WELCOME_ADMIN)
        return Admin()
    
    def _list_all_items(self):
        items = self._item_repository.all()
        self._show_items(items)

    def _list_all_customers(self):
        customers = self._customer_repository.all()
        self._show(LIST_CUSTOMERS)
        self._show('\n'.join([f"  {customer.id} - {customer.name}" for customer in customers]) + '\n')

    def _list_items_by_customer(self, customer_name):
        items = [Item(item.id, item.title) for item in self._item_repository.find_by_customer(customer_name)]
        self._show_items(items)

    def _list_my_orders(self):
        receipts = self._customer_repository.get_receipts(self.user.id)
        receipt_header = [
            RECEIPT_HEADER_1,
            RECEIPT_HEADER_2
        ]
        self._show_orders(LIST_ORDERS, receipt_header, receipts)

    def _list_all_orders(self):
        receipts = self._order_repository.get_receipts()
        receipt_header = [
            RECEIPT_HEADER_3,
            RECEIPT_HEADER_4
        ]
        self._show_orders(LIST_ORDERS_ADMIN, receipt_header, receipts)
    
    def _show_orders(self, preface, receipt_header, receipts):
        rows = receipt_header + receipts
        self._show(preface)
        self._show('\n'.join([str(row) for row in rows]) + '\n')

    def _add_item(self):
        name = self._prompt(PROMPT_NEW_ITEM_DESCRIPTION)
        unit_price = self._prompt(PROMPT_NEW_ITEM_UNIT_PRICE)
        quantity = self._prompt(PROMPT_NEW_ITEM_QUANTITY)
        item = Item(None, name, unit_price, quantity)
        self._item_repository.create(item)
        self._show(ITEM_ADDED_TO_SHOP)
    
    def _restock_item(self):
        self._list_all_items()
        item_id = self._prompt(PROMPT_RESTOCK_ITEM)
        qty = self._prompt(PROMPT_NEW_ITEM_QUANTITY)
        self._item_repository.update_quantity_stocked(item_id, qty)
        self._show(RESTOCK_CONFIRMATION)

    def _place_new_order(self):
        self._list_all_items()
        item_id = self._prompt(PROMPT_ORDER_ITEM)
        item = self._item_repository.find(item_id)
        item_qty = self._prompt(PROMPT_ORDER_QTY(item.quantity_stocked), int)

        order = Order(None, item_id, self.user.id, item_qty, date.today())
        if self._order_repository.create(order):
            self._show(ORDER_CONFIRMATION(item.unit_price * item_qty))
        else:
            self._show(ORDER_UNSUCCESSFUL)

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message, return_type=str):
        self.io.write(message + "\n")
        response = self.io.readline().strip()
        if response == 'q':
            raise ExitProgram
        else:
            return return_type(response)

    def _show_items(self, items):
        items_in_stock = [item for item in items if item.quantity_stocked > 0]
        if not any(items_in_stock):
            self._show(SOLD_OUT)

        show_qty = type(self.user) == Admin
        self._show(LIST_ITEMS)
        self._show('\n'.join([f"  {item.id} - {item.name :.<20} £{item.unit_price:.2f}{f'{item.quantity_stocked} in stock':>16}" if show_qty else f"  {item.id} - {item.name :.<20} £{item.unit_price:.2f}" for item in items_in_stock]) + '\n')

    def _invalid_response(self):
        self._show(INVALID_RESPONSE)


io = TerminalIO()

if __name__ == '__main__':
    connection = DatabaseConnection()
    connection.connect()
    app = Application(io, connection)
    app.run()