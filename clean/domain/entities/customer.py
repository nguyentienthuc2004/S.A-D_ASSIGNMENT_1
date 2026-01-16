class Customer:
  def __init__(self, name: str, email: str, password: str, id: int | None = None):
      self.id = id
      self.name = name
      self.email = email
      self.password = password
