from products import Product

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Only {self.maximum} allowed per order.")
        return super().buy(quantity)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}")