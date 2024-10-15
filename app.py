import sys
from lib.database_connection import DatabaseConnection
from lib.item import Item
from lib.customer import Customer
from lib.item_repository import ItemRepository
from lib.customer_repository import CustomerRepository
from lib.order_repository import OrderRepository

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
        self._show("Welcome to the shop management program!")
        self.user = self._get_user()
        if type(self.user) == Customer:
            self._customer_menu()

    def _customer_menu(self):
        while True:
            try:
                response = self._prompt("What would you like to do?\n  1 - List all shop items\n  2 - See your past orders\n  3 - Place a new order\n  4 - Delete my account\n  q - Exit")

                if response == "1":
                    self._list_all_items()
                elif response == "2":
                    customers = self._customer_repository.all()
                    customer_name = self._prompt_for_customer(customers)
                    self._list_items_by_customer(customer_name)
                elif response == "4":
                    self._delete_account()
                else:
                    self.__invalid_response()
            except:
                break

    def _get_user(self):
        while True:
            response = self._prompt("Are you a new or a returning customer? (n/r)").lower()

            if response == 'n':
                return self._create_new_customer()
            elif response == 'r':
                customer = self._prompt_for_id()
                if customer is not None:
                    return customer
            else:
                self._invalid_response()


    def _list_all_items(self):
        items = self._item_repository.all()
        self._show_items(items)

    def _create_new_customer(self):
        customer_name = self._prompt("What is your name?")
        id = self._customer_repository.create(Customer(None, customer_name))
        self._show(f"{customer_name}, your account has been created! Your ID number is {id}.")

    def _delete_account(self):
        response = self._prompt("This will delete your account permanently! Are you sure you want to proceed? (y/n)")
        if response.lower() == "y":
            self._show(f"Your account was deleted. Goodbye forever, {self.user.name}!")
            self._customer_repository.delete(self.user.id)
            raise ExitProgram

    def _prompt_for_id(self):
        customer_ids = [str(customer.id) for customer in self._customer_repository.all()]
        response = self._prompt("Please log in with your customer id:")

        if response in customer_ids:
            customer = self._customer_repository.find(int(response))
            self._show(f"Welcome back, {customer.name}!")
            return customer
        self._invalid_response()

    def _prompt_for_customer(self, customers):
        for customer in customers:
            self._show(f" * {customer.name}")

        return self._prompt("Select a customer: ")
    
    def _list_items_by_customer(self, customer_name):
        items = [Item(item.id, item.title) for item in self._item_repository.find_by_customer(customer_name)]
        self._show_items(items)

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        response = self.io.readline().strip()
        if response == 'q':
            raise ExitProgram
        else:
            return response

    def _show_items(self, items):
        items_in_stock = [item for item in items if item.quantity_stocked > 0]
        if not any(items_in_stock):
            self._show(" Sorry, we're sold out of everything today!.")

        self._show('We stock the following items:')
        self._show('\n'.join([f"  {item.id} - {item.name :.<20} £{item.unit_price}" for item in items_in_stock]) + '\n')
    
    def _invalid_response(self):
        self._show("That's not a valid response!")


io = TerminalIO()

if __name__ == '__main__':
    connection = DatabaseConnection()
    connection.connect()
    app = Application(io, connection)
    app.run()