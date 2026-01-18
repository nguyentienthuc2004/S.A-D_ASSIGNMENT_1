from domain.repositories.customers.customer_repository import CustomerRepository
from infrastructure.customer.models import CustomerModel
from domain.entities.customer import Customer
class CustomerRepositoryImpl(CustomerRepository):
    def find_by_email(self, email):
      try:
        obj = CustomerModel.objects.get(email=email)
        return Customer(
            id=obj.id,
            name=obj.name,
            email=obj.email,
            password=obj.password
        )
      except CustomerModel.DoesNotExist:
        return None
    def save(self, customer):
      obj = CustomerModel.objects.create(
            name=customer.name,
            email=customer.email,
            password=customer.password
        )
      return Customer(
          id=obj.id,
          name=obj.name,
          email=obj.email,
          password=obj.password
      )
  