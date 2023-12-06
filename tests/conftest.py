# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import json
import pytest

from testlib.api import BaseUrl, User


# --------------------------------------------------------------------------------
# Private Functions
# --------------------------------------------------------------------------------

def _build_user(inputs, index):
  users = inputs['users']
  user = User(users[index]['id'], users[index]['email'], users[index]['password'])
  return user


# --------------------------------------------------------------------------------
# Config Fixture
# --------------------------------------------------------------------------------

@pytest.fixture(scope='session')
def test_inputs():
  with open('inputs.json') as config_json:
    data = json.load(config_json)
  return data


@pytest.fixture
def base_url(test_inputs):
  return BaseUrl(test_inputs['base_url'])


@pytest.fixture
def valid_user(test_inputs):
  return _build_user(test_inputs, 0)


@pytest.fixture
def invalid_user(test_inputs):
  return _build_user(test_inputs, 1)