
from django.urls import path
from .views import get_list_books
urlpatterns = [
    path('',get_list_books, name='list_books'),
]
