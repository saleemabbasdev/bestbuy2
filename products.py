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
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

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

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return float(total_price)
