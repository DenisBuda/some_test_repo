from json_schema import json_schema
import requests

my_url = "https://www.google.ru/"


def test_function():
    assert requests.get(my_url).status_code
    print(requests.get(my_url).status_code)

# test_function(my_url)








