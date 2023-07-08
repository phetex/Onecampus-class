class Product:
    def __init__(self, name, price, discount=0, special_offer=False, quantity_price=None):
        self.name = name
        self.price = price
        self.discount = discount
        self.special_offer = special_offer
        self.quantity_price = quantity_price

    def calculate_price(self, quantity):
        if self.quantity_price and quantity >= self.quantity_price['quantity']:
            return self.quantity_price['price']
        else:
            discounted_price = self.price - (self.price * self.discount)
            return discounted_price

# Create some sample products with pricing features
product1 = Product("Shirt", 20.99)
product2 = Product("Jeans", 39.99, discount=0.1)  # 10% discount
product3 = Product("Shoes", 49.99, special_offer=True)  # Special offer product
product4 = Product("Socks", 4.99, quantity_price={'quantity': 3, 'price': 12.99})  # Quantity pricing

# Calculate the prices for different quantities
quantity1 = 1
price1 = product1.calculate_price(quantity1)
print(f"Price for {quantity1} {product1.name}: ${price1}")

quantity2 = 2
price2 = product2.calculate_price(quantity2)
print(f"Price for {quantity2} {product2.name}: ${price2}")

quantity3 = 1
price3 = product3.calculate_price(quantity3)
print(f"Price for {quantity3} {product3.name}: ${price3}")

quantity4 = 4
price4 = product4.calculate_price(quantity4)
print(f"Price for {quantity4} {product4.name}: ${price4}")
