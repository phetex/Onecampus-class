from datetime import datetime

class GoodsReceiveNote:
    def __init__(self, supplier, items):
        self.supplier = supplier
        self.items = items
        self.received_date = datetime.now()

    def print_grn(self):
        print("Goods Receive Note")
        print("Supplier:", self.supplier)
        print("Received Date:", self.received_date.strftime("%Y-%m-%d %H:%M:%S"))
        print("Items:")
        for item in self.items:
            print("- Name:", item['name'])
            print("  Quantity:", item['quantity'])
            print("  Unit Price:", item['unit_price'])
            print()

# Example usage
supplier = "ABC Supplier"
items = [
    {"name": "Product A", "quantity": 10, "unit_price": 15.99},
    {"name": "Product B", "quantity": 5, "unit_price": 9.99},
    {"name": "Product C", "quantity": 2, "unit_price": 24.99}
]

grn = GoodsReceiveNote(supplier, items)
grn.print_grn()
