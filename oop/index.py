class item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = item("Phone", 100, 5)
item2 = item("Laptop", 1000, 3)


