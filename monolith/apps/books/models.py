from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title
