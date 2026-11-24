from products import Product

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        pass  # quantity always stays 0

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        return float(quantity * self.price)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: Unlimited")
