class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

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
        print("Placing order for customer:", self.customer)
        print("Total amount:", total)

        # Add code for additional order processing steps (e.g., payment, shipping, etc.)

# Create some sample products
product1 = Product("Shirt", 20.99)
product2 = Product("Jeans", 39.99)
product3 = Product("Shoes", 49.99)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_item(product1, 2)
cart.add_item(product2, 1)

# Remove a product from the cart
cart.remove_item(product1)

# Calculate the total amount in the cart
total_amount = cart.calculate_total()
print("Total amount in the cart:", total_amount)

# Create an order for the shopping cart
customer_name = "John Doe"
order = Order(customer_name, cart)

# Place the order
order.place_order()
