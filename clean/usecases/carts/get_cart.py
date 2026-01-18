
class GetCartUseCase:
  def __init__(self, cart_repository):
    self.cart_repository = cart_repository

  def execute(self, customer_id):
    return self.cart_repository.get_cart(customer_id)