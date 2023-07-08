class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    def has_permission(self, required_role):
        return self.role == required_role or self.role == 'admin'

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart

    def place_order(self):
        total = self.cart.calculate_total()
        print("Placing order for customer:", self.customer.username)
        print("Total amount:", total)

        # Add code for additional order processing steps (e.g., payment, shipping, etc.)

# Create some sample products
product1 = Product("Shirt", 20.99)
product2 = Product("Jeans", 39.99)

# Create a shopping cart
cart = ShoppingCart()

# Create some sample users with different roles
admin_user = User("admin", "admin123", "admin")
customer_user = User("customer", "pass123", "customer")

# Authenticate the user
username = input("Enter your username: ")
password = input("Enter your password: ")
if customer_user.authenticate(username, password):
    print("Authentication successful.")
    # Add products to the cart
    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    # Create an order for the shopping cart
    order = Order(customer_user, cart)

    # Place the order if the user has permission
    if customer_user.has_permission('customer'):
        order.place_order()
    else:
        print("User does not have permission to place orders.")
else:
    print("Authentication failed.")
