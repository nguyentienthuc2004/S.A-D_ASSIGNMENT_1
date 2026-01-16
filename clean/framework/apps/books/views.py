from django.shortcuts import render
from interfaces.controllers.books.book_controller import BookController
# Create your views here.
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'home.html')
def get_list_books(request):
    controller = BookController()
    books = controller.get_list_books()
    return render(request, 'books/list_books.html', {
        'books': books
    })
