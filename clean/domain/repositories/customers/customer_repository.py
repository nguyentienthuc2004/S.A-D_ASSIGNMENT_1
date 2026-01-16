from abc import ABC, abstractmethod

class CustomerRepository(ABC):
  @abstractmethod
  def authen(self, email, password):
    pass
  @abstractmethod
  def exists_by_email(self, email):
    pass
  @abstractmethod
  def save(self, customer):
    pass