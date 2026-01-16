
class Cart:
  def __init__(self, id, customer, created_at=None, items=None):
    self.id = id
    self.customer = customer
    self.created_at = created_at
    self.items = items if items is not None else []
  def add_item(self, cart_item):
    self.items.append(cart_item)
  @property
  def total_price(self):
    return sum(item.total_price for item in self.items)
