from interfaces.controllers.carts.cart_controller import CartController
def cart_item_count(request):
    customer_id = request.session.get('customer_id')
    count=0
    if customer_id:
        controller = CartController()
        count = controller.get_list_cartitems(customer_id).__len__()
    return {
        'cart_item_count': count
    }
