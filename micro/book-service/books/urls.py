
from django.urls import path
from .views import get_list_books,get_book
urlpatterns = [
    path('',get_list_books, name='list_books'),
    path('<int:book_id>/',get_book, name='book_detail'),
]
