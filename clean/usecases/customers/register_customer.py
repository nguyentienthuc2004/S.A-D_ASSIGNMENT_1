
from domain.entities.customer import Customer
class RegisterCustomerUseCase:
  def __init__(self,customer_repository):
    self.customer_repository = customer_repository
  def execute(self,name,email,password):
    customer = self.customer_repository.find_by_email(email)
    if customer:
      raise Exception("Email already registered")
    customer = Customer(None,name=name,email=email,password=password)
    return self.customer_repository.save(customer)
