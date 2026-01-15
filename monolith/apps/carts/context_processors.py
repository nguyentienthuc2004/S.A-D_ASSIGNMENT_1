from .models import CartItem

def cart_item_count(request):
    if request.session.get('customer_id'):
        count = CartItem.objects.filter(
            cart__customer_id=request.session['customer_id']
        ).count()
    else:
        count = 0

    return {
        'cart_item_count': count
    }
