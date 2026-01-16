class CartItem:
    def __init__(self, id, book, quantity):
        self.id = id
        self.book = book
        self.quantity = quantity

    @property
    def total_price(self):
        return self.quantity * self.book.price