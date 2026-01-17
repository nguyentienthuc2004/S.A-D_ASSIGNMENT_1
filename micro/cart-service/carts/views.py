from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from .models import Cart, CartItem
import requests
@api_view(['POST'])
def add_to_cart(request):
    customer_id = request.data.get('customer_id')
    book_id = request.data.get('book_id')
    quantity = request.data.get('quantity', 1)

    if not customer_id or not book_id:
        return Response(
            {'error': 'Missing customer_id or book_id'},
            status=400
        )

    # 1️⃣ Lấy hoặc tạo cart cho customer
    cart, _ = Cart.objects.get_or_create(
        customer_id=customer_id
    )

    # 2️⃣ Lấy hoặc tạo cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        book_id=book_id,
        defaults={'quantity': quantity}
    )

    if not created:
        cart_item.quantity += int(quantity)
        cart_item.save()

    return Response({
        'message': 'Added to cart successfully',
        'cart_id': cart.id,
        'book_id': book_id,
        'quantity': cart_item.quantity
    }, status=201)

@api_view(['GET'])
def view_cart(request):
    customer_id = request.query_params.get('customer_id')

    if not customer_id:
        return Response(
            {'error': 'Missing customer_id'},
            status=400
        )

    cart = Cart.objects.filter(customer_id=customer_id).first()

    if not cart:
        return Response({
            'cart_items': [],
            'total_price': 0
        })

    items = CartItem.objects.filter(cart=cart)

    result = []
    total_price = 0

    for item in items:
        book = requests.get(
            f"http://localhost:8002/books/{item.book_id}/"
        ).json()

        item_total = item.quantity * book['price']
        total_price += item_total

        result.append({
            'book_id': item.book_id,
            'title': book['title'],
            'price': book['price'],
            'quantity': item.quantity,
            'total_price': item_total
        })

    return Response({
        'cart_id': cart.id,
        'customer_id': customer_id,
        'items': result,
        'total_price': total_price
    })
