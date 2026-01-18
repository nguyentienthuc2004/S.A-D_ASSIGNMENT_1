from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from datetime import date
from interfaces.controllers.carts.cart_controller import CartController
# Create your views here.
def add_to_cart(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('/customer/login/')
    book_id = request.POST.get('book_id')
    controller = CartController()
    controller.add_cartitem(customer_id, book_id, 1)
    return redirect('/books/')

def view_cart(request):
  customer_id = request.session.get('customer_id')
  if not customer_id:
      return redirect('/customer/login/')
  controller = CartController()
  cart = controller.get_cart(customer_id)
  items = cart.items
  return render(request, 'carts/view_cart.html', {
      'cart_items': items
  })