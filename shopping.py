

# Class
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
        return "\n".join([item.get_info() for item in self.items])


class Payment():
    def __init__(self, client, cart):
        self.client = client
        self.cart = cart
        self.status = "Pending"

    def process_payment(self, client, cart):
        if cart.total > client.total:
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