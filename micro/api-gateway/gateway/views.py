import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
CUSTOMER_SERVICE_URL = "http://localhost:8001/customers"
BOOK_SERVICE_URL = "http://localhost:8002/books"
CART_SERVICE_URL = "http://localhost:8003/carts"
@csrf_exempt
def register_customer(request):
    data = json.loads(request.body)

    response = requests.post(
        f"{CUSTOMER_SERVICE_URL}/register/",
        json=data
    )

    return JsonResponse(response.json(), status=response.status_code)

@csrf_exempt
def login_customer(request):
    data = json.loads(request.body)

    response = requests.post(
        f"{CUSTOMER_SERVICE_URL}/login/",
        json=data
    )

    return JsonResponse(response.json(), status=response.status_code)

@csrf_exempt
def get_list_books(request):
    response = requests.get(f"{BOOK_SERVICE_URL}/")
    return JsonResponse(response.json(), safe=False, status=response.status_code)

@csrf_exempt
def add_cart_item(request):
    data = json.loads(request.body)

    response = requests.post(
        f"{CART_SERVICE_URL}/add/",
        json=data
    )

    return JsonResponse(response.json(), status=response.status_code)
@csrf_exempt
def view_cart(request):
    customer_id = request.GET.get('customer_id')

    response = requests.get(
        f"{CART_SERVICE_URL}/",
        params={'customer_id': customer_id}
    )

    return JsonResponse(response.json(), status=response.status_code)
