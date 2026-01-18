from usecases.carts.get_cart import GetCartUseCase
from infrastructure.carts.cart_repository_impl import CartRepositoryImpl
from infrastructure.books.book_impl import BookRepositoryImpl
from usecases.carts.add_cartitem import AddCartItemUseCase
class CartController:
  def get_cart(self, customer_id):
    cartRepo = CartRepositoryImpl()
    usecase = GetCartUseCase(cartRepo)
    return usecase.execute(customer_id)
  def add_cartitem(self, customer_id, book_id, quantity):
    cartRepo = CartRepositoryImpl()
    bookRepo = BookRepositoryImpl()
    usecase = AddCartItemUseCase(cartRepo, bookRepo)
    return usecase.execute(customer_id, book_id, quantity)