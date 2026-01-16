from domain.repositories.customers.customer_repository import CustomerRepository
from infrastructure.customer.models import CustomerModel

class CustomerRepositoryImpl(CustomerRepository):
    def authen(self, email, password):
      customer = CustomerModel.objects.get(
        email=email,password=password
      )
      return customer
    def exists_by_email(self, email):
      return CustomerModel.objects.filter(email=email).exists()
    def save(self, customer):
      obj = CustomerModel.objects.create(
        name=customer.name,
        email=customer.email,
        password=customer.password
      )
      obj.save()
      customer.id = obj.id
      return customer
  