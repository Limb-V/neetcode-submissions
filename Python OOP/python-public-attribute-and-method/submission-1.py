class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Add: name, price
    def call_price(self):
        print(f"{self.price}")

chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
print(chips.name)
chips.call_price()