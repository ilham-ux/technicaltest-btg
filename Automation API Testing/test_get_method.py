import requests
import pytest

def test_get_method():
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

Code = response.status_code

assert Code == 200