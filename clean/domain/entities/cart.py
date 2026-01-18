from domain.entities.cartitem import CartItem
class Cart:
    def __init__(self, id, customer, items=None):
      self.id = id
      self.customer = customer
      self.items = items or []

    def add_item(self, book, quantity):
      for item in self.items:
          if item.book.id == book.id:
              item.increase(quantity)
              return
      self.items.append(CartItem(book, quantity))
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)

