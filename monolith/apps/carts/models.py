from django.db import models
from apps.customers.models import Customer
from apps.books.models import Book
# Create your models here.

class Cart(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  customer = models.ForeignKey(Customer,  on_delete=models.CASCADE, db_column='CustomerID')

  class Meta:
    db_table = 'cart'
  
  def __str__(self):
    return f'Cart {self.id} for {self.customer.name}'
  

class CartItem(models.Model):
  quantity = models.IntegerField()
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, db_column='CartID')
  book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='BookID')
  
  class Meta: 
    db_table = 'cartitem'
  
  def __str__(self):
    return f'{self.quantity} of {self.book.title} in cart {self.cart.id}'
  @property
  def total_price(self):
    return self.quantity * self.book.price