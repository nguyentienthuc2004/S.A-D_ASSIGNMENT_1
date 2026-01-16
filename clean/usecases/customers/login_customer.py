
class LoginCustomerUseCase:
  def __init__(self, repo):
    self.repo = repo

  def authen(self, email, password):
    customer = self.repo.authen(email, password)
    if not customer:
      raise Exception("Authentication failed")
    return customer