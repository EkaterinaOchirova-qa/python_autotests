import pytest
import requests


def test_status_code():
    url = "https://petstore.swagger.io/v2/pet/16"
    response = requests.get(url)
    assert response.status_code == 200


def test_check_response():
    url = "https://petstore.swagger.io/v2/pet/16"
    response = requests.get(url)
    response = response.json()
    assert response["name"] == "bunny"