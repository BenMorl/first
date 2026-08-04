# CLASSES
class Client():
    def __init__(self, name, email, money):
        self.name = name
        self.email = email
        self.money = money

    def get_info(self):
        return f"Client: {self.name} | Email: {self.email}"
    

class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Item: {self.name} | Price: ${self.price:.2f}"
    

class Cart():
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        self.sum_total(item.price)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.sum_total(-item.price)

    def sum_total(self, price):
        self.total += price

    def show_cart(self):
        if not self.items:
            return "Cart is empty."
        print("\n".join([item.get_info() for item in self.items]))


class Payment():
    def __init__(self, client, cart):
        self.client = client
        self.cart = cart
        self.status = "Pending"

    def process_payment(self):
        if self.cart.total > self.client.money:
            print("Insufficient funds for this transaction.")
            return False
        self.status = "Completed"
        return True

    def get_info(self):
        return (
            f"\n===== PAYMENT =====\n"
            f"Client: {self.client.name}\n"
            f"Total Amount: ${self.cart.total:.2f}\n"
            f"Status: {self.status}"
        )

# Options menu
def menu():
    print("\n===== SHOPPING MENU =====")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")

# Inputs functions
def input_name() -> str:
    name = input("Enter your name: ")
    return name

def input_email() -> str:
    email = input("Enter your email: ")
    return email

def input_money() -> float:
    while True:
        try:
            money = float(input("Enter your available funds: "))
            return money
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def input_item_name() -> str:
    item_name = input("Enter the item name: ")
    return item_name


def input_item_price() -> float:
    while True:
        try:
            item_price = float(input("Enter the item price: "))
            return item_price
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def input_option() -> str:
    option = input("Select an option: ")
    return option

# Functions for the shopping flow
def create_item():
    name = input_item_name()
    price = input_item_price()
    return Item(name, price)
      
          
def remove_item_from_cart(cart):
    if not cart.items:
        print("Cart is empty. No items to remove.")
        return

    cart.show_cart()
    item_name = input_item_name()

    for item in cart.items:
        if item.name == item_name:
            cart.remove_item(item)
            print(f"Removed {item.name} from the cart.")
            return

    print(f"Item '{item_name}' not found in the cart.")


def checkout(client, cart):
    if not cart.items:
        print("Cart is empty. Cannot proceed to checkout.")
        return
    
    payment = Payment(client, cart)
    if payment.process_payment():
        print(payment.get_info())
        print("Checkout successful!")
    else:
        print("Checkout failed due to insufficient funds.")

# Main
def purchase_flow():
    # Objects
    client = Client(input_name(), input_email(), input_money())
    cart = Cart()
    
    while True:
        menu()
        option = input_option()
        match option:
            case "1":
                cart.add_item(create_item())
            case "2":
                remove_item_from_cart(cart)
            case "3":
                cart.show_cart()
            case "4":
                checkout(client, cart)
            case "5":
                print("Thank you for shopping with us!")
                break


if __name__ == "__main__":
    purchase_flow()

