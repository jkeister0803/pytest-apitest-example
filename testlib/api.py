# --------------------------------------------------------------------------------
# Class: BaseUrl
# --------------------------------------------------------------------------------

class BaseUrl:
  
  def __init__(self, base_url):
    self.base_url = base_url
  
  def concat(self, resource):
    return self.base_url + resource


# --------------------------------------------------------------------------------
# Class: User
# --------------------------------------------------------------------------------

class User:

  def __init__(self, id, email, password):
    self.id = id
    self.email = email
    self.password = password