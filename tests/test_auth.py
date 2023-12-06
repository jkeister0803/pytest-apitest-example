# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import requests
from testlib.api import BaseUrl, User

# --------------------------------------------------------------------------------
# Helper Functions
# --------------------------------------------------------------------------------

def login(base_url, user):
  url = base_url.concat('/login')
  body = {
    'email': user.email,
    'password': user.password
  }
  return requests.post(url, body)

def logout(base_url):
  url = base_url.concat('/logout')
  return requests.post(url)

# --------------------------------------------------------------------------------
# Verification Functions
# --------------------------------------------------------------------------------

def verify_authorized(response):
  data = response.json()
  assert response.status_code == 200
  assert isinstance(data['token'], str)


def verify_unauthorized(response):
  data = response.json()
  assert response.status_code == 400
  assert data['error'] == 'user not found'


# --------------------------------------------------------------------------------
# Authentication Tests
# --------------------------------------------------------------------------------


def test_successful_login(base_url: BaseUrl, valid_user: User):
  response = login(base_url, valid_user)
  verify_authorized(response)


def test_unsuccessful_login(base_url: BaseUrl, invalid_user: User):
  response = login(base_url, invalid_user)
  verify_unauthorized(response)


def test_logout(base_url: BaseUrl):
  response = logout(base_url)
  assert response.status_code == 200