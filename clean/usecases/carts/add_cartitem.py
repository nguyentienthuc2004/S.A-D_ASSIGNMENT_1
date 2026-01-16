
class addCartItemUseCase:
  def __init__(self, cart_repository):
    self.cart_repository = cart_repository

  def execute(self,customer_id, book_id, quantity):
    return self.cart_repository.add_cartitem(customer_id,book_id, quantity)