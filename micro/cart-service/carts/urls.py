from django.urls import path
from .views import add_to_cart, view_cart
urlpatterns = [
  path('add/',add_to_cart, name='cart_add'),
  path('',view_cart, name='view_cart'),
]
