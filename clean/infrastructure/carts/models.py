from django.db import models
from infrastructure.customer.models import CustomerModel
from infrastructure.books.models import BookModel
# Create your models here.

class CartModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  customer = models.ForeignKey(CustomerModel,  on_delete=models.CASCADE, db_column='CustomerID')

  class Meta:
    db_table = 'cart'
    app_label = "persistence_app"
  
  def __str__(self):
    return f'Cart {self.id} for {self.customer.name}'
  

class CartItemModel(models.Model):
  quantity = models.IntegerField()
  cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, db_column='CartID')
  book = models.ForeignKey(BookModel, on_delete=models.CASCADE, db_column='BookID')
  
  class Meta: 
    db_table = 'cartitem'
    app_label = "persistence_app"
  
  def __str__(self):
    return f'{self.quantity} of {self.book.title} in cart {self.cart.id}'
  @property
  def total_price(self):
    return self.quantity * self.book.price