
from domain.repositories.books.book_repository import BooksRepository
from infrastructure.books.models import BookModel
class BookRepositoryImpl(BooksRepository):
    def get_all_books(self):
        return BookModel.objects.all()