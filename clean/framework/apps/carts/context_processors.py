from interfaces.controllers.carts.cart_controller import CartController
def cart_item_count(request):
    customer_id = request.session.get('customer_id')
    count=0
    if customer_id:
        controller = CartController()
        cart = controller.get_cart(customer_id)
        count = len(cart.items)
    return {
        'cart_item_count': count
    }
