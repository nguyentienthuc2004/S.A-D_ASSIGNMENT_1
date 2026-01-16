from django.urls import path
from framework.apps.customers.views import register_customer,login_customer ,logout_customer
urlpatterns = [
    path('register/',register_customer, name ='register_customer'),
    path('login/',login_customer, name ='login_customer'),
    path('logout/',logout_customer, name ='logout_customer'),
]
