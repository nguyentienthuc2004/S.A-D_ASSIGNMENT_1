from domain.repositories.carts.cart_repository import CartRepository
from usecases.carts.get_list_cartitems import getListCartItemsUseCase
from infrastructure.carts.cart_repository_impl import CartRepositoryImpl
from usecases.carts.add_cartitem import addCartItemUseCase
class CartController:
  def get_list_cartitems(self, customer_id):
    repo = CartRepositoryImpl()
    usecase = getListCartItemsUseCase(repo)
    return usecase.execute(customer_id)
  def add_cartitem(self, customer_id, book_id, quantity):
    repo = CartRepositoryImpl()
    from usecases.carts.add_cartitem import addCartItemUseCase
    usecase = addCartItemUseCase(repo)
    return usecase.execute(customer_id, book_id, quantity)