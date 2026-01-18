
from domain.repositories.books.book_repository import BooksRepository
from infrastructure.books.models import BookModel
from domain.entities.book import Book
class BookRepositoryImpl(BooksRepository):
    def get_all_books(self):
        books= BookModel.objects.all()
        return [
            Book(
                id=book.id,
                title=book.title,
                author=book.author,
                stock=book.stock,
                price=book.price
            )
            for book in books
        ]
    def get_book_by_id(self, book_id):
        book = BookModel.objects.get(id=book_id)
        return Book(
            id=book.id,
            title=book.title,
            author=book.author,
            stock=book.stock,
            price=book.price
        )