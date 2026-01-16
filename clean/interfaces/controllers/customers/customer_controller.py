
from infrastructure.customer.customer_impl import CustomerRepositoryImpl
from usecases.customers.register_customer import RegisterCustomerUseCase
from usecases.customers.login_customer import LoginCustomerUseCase
class CustomerController:
  def register_customer(self,name,email,password):
    
    repo = CustomerRepositoryImpl()
    usecase = RegisterCustomerUseCase(repo)
    
    return usecase.execute(name,email,password)
  def authen(self, email,password):
    
    repo = CustomerRepositoryImpl()
    usecase = LoginCustomerUseCase(repo)
    return usecase.authen(email,password)
    
    
    