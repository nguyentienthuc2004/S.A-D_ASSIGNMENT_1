from domain.repositories.carts.cart_repository import CartRepository
from infrastructure.carts.models import CartItemModel, CartModel
from datetime import date
from django.shortcuts import render

class CartRepositoryImpl(CartRepository):
  def get_list_cartitems(self,customer_id):
    cart, created = CartModel.objects.get_or_create(
        customer_id=customer_id,
        defaults={'created_at': date.today()}
    )

    cart_items = CartItemModel.objects.filter(cart=cart)
    return cart_items
  def add_cartitem(self, customer_id, book_id, quantity):
    cart, created = CartModel.objects.get_or_create(
        customer_id=customer_id,
        defaults={'created_at': date.today()}
    )
    cart_item, created = CartItemModel.objects.get_or_create(
        cart=cart,
        book_id=book_id,
        defaults={'quantity': quantity}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    return cart_item