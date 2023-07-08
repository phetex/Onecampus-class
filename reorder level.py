class Product:
    def __init__(self, name, price, reorder_level=10):
        self.name = name
        self.price = price
        self.reorder_level = reorder_level

    def is_below_reorder_level(self, quantity):
        if quantity < self.reorder_level:
            return True
        else:
            return False

# Create some sample products with reorder level
product1 = Product("Shirt", 20.99)
product2 = Product("Jeans", 39.99, reorder_level=5)
product3 = Product("Shoes", 49.99)

# Check if products are below reorder level
quantity1 = 3
below_reorder1 = product1.is_below_reorder_level(quantity1)
print(f"Product {product1.name} is below reorder level: {below_reorder1}")

quantity2 = 2
below_reorder2 = product2.is_below_reorder_level(quantity2)
print(f"Product {product2.name} is below reorder level: {below_reorder2}")

quantity3 = 12
below_reorder3 = product3.is_below_reorder_level(quantity3)
print(f"Product {product3.name} is below reorder level: {below_reorder3}")
