from abc import ABC, abstractmethod

class BooksRepository(ABC):
  @abstractmethod
  def get_all_books(self):
    pass
  @abstractmethod
  def get_book_by_id(self, book_id):
    pass