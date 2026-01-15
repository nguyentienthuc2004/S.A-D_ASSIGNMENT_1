from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer
# Create your views here.

def register_customer(request):
  if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate đơn giản
        if not name or not email or not password:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin.')
            return render(request, 'customers/register.html')

        # Kiểm tra email đã tồn tại chưa
        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'Email đã tồn tại.')
            return render(request, 'customers/register.html')
        Customer.objects.create(
            name=name,
            email=email,
            password=password
        )

        messages.success(request, 'Đăng ký thành công. Vui lòng đăng nhập.')
        return redirect('customers/login')
  return render(request,'customers/register.html')

def login_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Kiểm tra thông tin đăng nhập
        try:
            customer = Customer.objects.get(email=email, password=password)
            # Lưu thông tin khách hàng vào session
            request.session['customer_id'] = customer.id
            messages.success(request, 'Đăng nhập thành công.')
            return redirect('home')  # Chuyển hướng đến trang chủ hoặc trang mong muốn
        except Customer.DoesNotExist:
            messages.error(request, 'Email hoặc mật khẩu không đúng.')
            return render(request, 'customers/login.html')

    return render(request, 'customers/login.html')
  
def logout_customer(request):
    # Xóa thông tin khách hàng khỏi session
    if 'customer_id' in request.session:
        del request.session['customer_id']
    messages.success(request, 'Đăng xuất thành công.')
    return redirect('home')  # Chuyển hướng đến trang chủ hoặc trang mong muốn