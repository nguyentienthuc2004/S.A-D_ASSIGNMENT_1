"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from gateway.views import register_customer, login_customer, get_list_books, add_cart_item, view_cart

urlpatterns = [
    path('customers/register/', register_customer),
    path('customers/login/', login_customer),
    path('books/', get_list_books),
    path('carts/add/', add_cart_item),
    path('carts/view_cart/', view_cart),
]
