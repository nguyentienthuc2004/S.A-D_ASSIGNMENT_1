from abc import ABC, abstractmethod

class CustomerRepository(ABC):
  @abstractmethod
  def find_by_email(self, email):
    pass
  @abstractmethod
  def save(self, customer):
    pass