class Customer:
  def __init__(self, id, name: str, email: str, password: str ):
      self.id = id
      self.name = name
      self.email = email
      self.password = password
  def check_password(self, raw_password: str) -> bool:
      return self.password == raw_password