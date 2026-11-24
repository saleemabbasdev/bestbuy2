class Product:

    # Initializations
    def __init__(self, name, price, quantity):

        if not name:
            raise ValueError("Name cannot be empty")

        if price < 0.0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    # Methods
    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        if self.active:
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{self.promotion_text()}")

    def buy(self, quantity: int) -> float:
        """
            Buys a given quantity of the product.
            Returns the total price (float) of the purchase.
            Updates the quantity of the product.
            In case of a problem (when? think about it), raises an Exception.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")

        if quantity > self.quantity:
            raise ValueError(f"Not enough stock! Available: {self.quantity}, Requested: {quantity}")

        total_price = self.calculate_price(quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price


# Promitions Methods
    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def promotion_text(self) -> str:
        return f", Promotion: {self.promotion.name}" if self.promotion else ""

    def calculate_price(self, quantity: int) -> float:
        if self.promotion:
            return float(self.promotion.apply_promotion(self, quantity))
        return float(quantity * self.price)



class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        pass  # quantity always stays 0

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        return self.calculate_price(quantity)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: Unlimited{self.promotion_text()}")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Only {self.maximum} allowed per order.")
        return super().buy(quantity)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, ")

