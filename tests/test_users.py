# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import requests
from testlib.api import BaseUrl, User

# --------------------------------------------------------------------------------
# Helper Functions
# --------------------------------------------------------------------------------

def get_users(base_url):
  url = base_url.concat('/users')
  return requests.get(url)

def get_user(base_url, user_id):
  url = base_url.concat('/users/' + user_id)
  return requests.get(url)

def update_user(base_url, user_id, user_info):
  url = base_url.concat('/users/' + user_id)
  return requests.put(url, json=user_info)

def delete_user(base_url, user_id):
  url = base_url.concat('/users/' + user_id)
  return requests.delete(url)

def register_user(base_url, user):
  url = base_url.concat('/register')
  body = {
    'email': user.email,
    'password': user.password
  }
  return requests.post(url, body)


# --------------------------------------------------------------------------------
# User Tests
# --------------------------------------------------------------------------------


def test_get_users(base_url: BaseUrl):
  response = get_users(base_url)
  data = response.json()
  assert response.status_code == 200
  assert data['total'] == 12


def test_get_single_user_successful(base_url: BaseUrl, valid_user: User):
  response = get_user(base_url, valid_user.id)
  data = response.json()
  assert response.status_code == 200
  assert data['data']['email'] == valid_user.email


def test_get_single_user_unsuccessful(base_url: BaseUrl, invalid_user: User):
  response = get_user(base_url, invalid_user.id)
  data = response.json()
  assert response.status_code == 404
  assert data == {}


def test_update_single_user(base_url: BaseUrl, valid_user: User):
  updated_user_info = {
    'name': 'zeus',
    'job': 'king of gods',
    'location': 'mount olympus'
  }
  response = update_user(base_url, valid_user.id, updated_user_info)
  data = response.json()
  assert response.status_code == 200
  assert data['name'] == updated_user_info['name']
  assert data['job'] == updated_user_info['job']
  assert data['location'] == updated_user_info['location']
  

def test_delete_single_user(base_url: BaseUrl, valid_user: User):
  response = delete_user(base_url, valid_user.id)
  assert response.status_code == 204


def test_register_existing_user_successful(base_url: BaseUrl, valid_user: User):
  response = register_user(base_url, valid_user)
  data = response.json()
  assert response.status_code == 200
  assert data['id'] == 1
  assert isinstance(data['token'], str)


def test_register_user_unsuccessful(base_url: BaseUrl, invalid_user: User):
  response = register_user(base_url, invalid_user)
  data = response.json()
  assert response.status_code == 400
  assert data['error'] == 'Note: Only defined users succeed registration'