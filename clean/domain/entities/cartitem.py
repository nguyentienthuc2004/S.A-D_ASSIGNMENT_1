class CartItem:
    def __init__(self, book, quantity):
        self.book = book
        self.quantity = quantity

    def increase(self, qty):
        self.quantity += qty

    @property
    def total_price(self):
        return self.book.price * self.quantity
