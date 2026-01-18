
class AddCartItemUseCase:
  def __init__(self, cart_repository, book_repository):
    self.cart_repository = cart_repository
    self.book_repository = book_repository

  def execute(self,customer_id, book_id, quantity):
    print('DEBUG: AddCartItemUseCase.execute called with customer_id={}, book_id={}, quantity={}'.format(customer_id, book_id, quantity))
    cart = self.cart_repository.get_cart(customer_id)
    book = self.book_repository.get_book_by_id(book_id)
    cart.add_item(book, quantity)
    self.cart_repository.save_cart(cart)
    
    