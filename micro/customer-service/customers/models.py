from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  
  class Meta:
    db_table = 'customer'
  
  def __str__(self):
    return self.name