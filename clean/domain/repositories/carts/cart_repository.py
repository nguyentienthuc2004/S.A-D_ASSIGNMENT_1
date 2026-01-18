
from abc import ABC, abstractmethod
class CartRepository(ABC):
  
  @abstractmethod
  def get_cart(self, customer_id):
    pass
  @abstractmethod
  def save_cart(self, cart):
    pass
  