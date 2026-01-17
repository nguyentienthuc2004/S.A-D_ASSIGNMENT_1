from django.db import models

# Create your models here.
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer_id = models.IntegerField()   # ID từ customer-service

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f'Cart {self.id} for customer {self.customer_id}'

class CartItem(models.Model):
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book_id = models.IntegerField()   # ID từ book-service

    class Meta:
        db_table = 'cartitem'

    @property
    def total_price(self):
        return self.quantity * self.book_price
