from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def register_customer(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    if not name or not email or not password:
        return Response({'error': 'Missing fields'}, status=400)

    if Customer.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=400)

    customer = Customer.objects.create(
        name=name,
        email=email,
        password=password
    )

    return Response({
        'id': customer.id,
        'name': customer.name,
        'email': customer.email
    }, status=201)

@api_view(['POST'])
def login_customer(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Missing fields'}, status=400)

    try:
        customer = Customer.objects.get(email=email, password=password)
    except Customer.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=401)

    return Response({
        'id': customer.id,
        'name': customer.name,
        'email': customer.email
    })
  
def logout_customer(request):
    # Xóa thông tin khách hàng khỏi session
    if 'customer_id' in request.session:
        del request.session['customer_id']
    messages.success(request, 'Đăng xuất thành công.')
    return redirect('home')  # Chuyển hướng đến trang chủ hoặc trang mong muốn