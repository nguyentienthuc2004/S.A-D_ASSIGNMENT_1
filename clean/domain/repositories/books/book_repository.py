from abc import ABC, abstractmethod

class BooksRepository(ABC):
  @abstractmethod
  def get_all_books(self):
    pass