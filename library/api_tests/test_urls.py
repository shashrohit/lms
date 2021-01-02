from os import environ
import requests


def test_list_books():
    service_url = environ.get("service_url")
    list_url = service_url + "/list-books"
    response = requests.get(list_url)
    assert response.status_code == 201
