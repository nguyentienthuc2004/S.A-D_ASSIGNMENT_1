from infrastructure.books.book_impl import BookRepositoryImpl
from usecases.books.get_list_books import getListBooksUseCase
class BookController:
  def get_list_books(self):
    
    repo = BookRepositoryImpl()
    usecase = getListBooksUseCase(repo)
    return usecase.execute()