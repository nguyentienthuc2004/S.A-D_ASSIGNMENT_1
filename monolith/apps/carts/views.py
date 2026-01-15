from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .models import Cart, CartItem
from apps.books.models import Book
from datetime import date

def add_to_cart(request):
    if request.method == 'POST':
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return redirect('/customer/login/')

        book_id = request.POST.get('book_id')
        book = Book.objects.get(id=book_id)

        # 1️⃣ Lấy hoặc tạo cart cho customer
        cart, created = Cart.objects.get_or_create(
            customer_id=customer_id,
            defaults={'created_at': date.today()}
        )

        # 2️⃣ Nếu sách đã có trong giỏ → tăng quantity
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('/books/')
def view_cart(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('/customer/login/')

    cart, created = Cart.objects.get_or_create(
        customer_id=customer_id,
        defaults={'created_at': date.today()}
    )

    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'carts/view_cart.html', {
        'cart_items': cart_items
    })