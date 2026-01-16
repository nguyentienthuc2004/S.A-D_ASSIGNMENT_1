from django.shortcuts import render, redirect
from django.contrib import messages
from interfaces.controllers.customers.customer_controller import CustomerController
# Create your views here.

def register_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # validate cơ bản (được phép ở view)
        if not name or not email or not password:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin.')
            return render(request, 'customers/register.html')

        controller = CustomerController()

        try:
            controller.register_customer(name, email, password)
            messages.success(
                request,
                'Đăng ký thành công. Vui lòng đăng nhập.'
            )
        except Exception as e:
            messages.error(request, str(e))
            return render(request, 'customers/register.html')

    return render(request, 'customers/register.html')

def login_customer(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        controller = CustomerController()
        try:
            customer = controller.authen(email,password)
            request.session['customer_id'] = customer.id
            request.session['customer_name'] = customer.name
            messages.success(request, 'Đăng nhập thành công.')
            return redirect('home')  # Chuyển hướng đến trang chủ hoặc trang mong muốn
        except Exception as e:
            messages.error(request, str(e))
            return render(request, 'customers/login.html')
    return render(request, 'customers/login.html')
  
def logout_customer(request):
    # Xóa thông tin khách hàng khỏi session
    if 'customer_id' in request.session:
        del request.session['customer_id']
    messages.success(request, 'Đăng xuất thành công.')
    return redirect('home')  # Chuyển hướng đến trang chủ hoặc trang mong mu ốn