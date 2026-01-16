from django.db import models

class CustomerModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'customer'
        app_label = "persistence_app"

    def __str__(self):
        return self.name