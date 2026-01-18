from domain.repositories.carts.cart_repository import CartRepository
from infrastructure.carts.models import CartItemModel, CartModel
from datetime import date
from django.shortcuts import render
from domain.entities.cart import Cart
from domain.entities.cartitem import CartItem
from infrastructure.books.models import BookModel

class CartRepositoryImpl(CartRepository):
  def get_cart(self,customer_id):
    cart, created = CartModel.objects.get_or_create(customer_id=customer_id)
    cart_items = CartItemModel.objects.filter(cart=cart)
    return Cart(
        id=cart.id,
        customer=cart.customer,
        items=[
            CartItem(
                book=item.book,
                quantity=item.quantity
            )
            for item in cart_items
        ]
    )
  def save_cart(self, cart):
    cart_model = CartModel.objects.get(id=cart.id)
    for item in cart.items:
        book = BookModel.objects.get(id=item.book.id)
        cart_item_model, created = CartItemModel.objects.get_or_create(
            cart=cart_model,
            book=book,
            defaults={'quantity': item.quantity}
        )
        if not created:
            cart_item_model.quantity =item.quantity
            cart_item_model.save()
        