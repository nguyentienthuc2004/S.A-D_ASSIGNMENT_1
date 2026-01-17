
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book

@api_view(['GET'])
def get_list_books(request):
    books = Book.objects.all()

    data = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'price': book.price
        }
        for book in books
    ]

    return Response(data)

@api_view(['GET'])
def get_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'price': book.price
    }

    return Response(data)
    