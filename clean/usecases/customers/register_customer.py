
from domain.entities.customer import Customer
class RegisterCustomerUseCase:
  def __init__(self,customer_repository):
    self.customer_repository = customer_repository
  def execute(self,name,email,password):
    if self.customer_repository.exists_by_email(email):
      raise Exception("Email already registered")
    customer = Customer(name=name,email=email,password=password)
    return self.customer_repository.save(customer)
