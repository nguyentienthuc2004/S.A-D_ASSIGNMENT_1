
class LoginCustomerUseCase:
  def __init__(self, repo):
    self.repo = repo

  def authen(self, email, password):
    print('DEBUG: LoginCustomerUseCase authen called with email=', email, ' password', password)
    customer = self.repo.find_by_email(email)
    print('DEBUG:', customer)
    if not customer:
      raise Exception("Email not found")
    if not customer.check_password(password):
      raise Exception("Incorrect password")
    return customer