
from abc import ABC, abstractmethod
class CartRepository(ABC):
  
  @abstractmethod
  def get_list_cartitems(self, customer_id):
    pass
  @abstractmethod
  def add_cartitem(self, customer_id,book_id, quantity):
    pass
  