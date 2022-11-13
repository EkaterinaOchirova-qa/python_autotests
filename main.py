import requests


# Создание питомца
data_petstore = {"id": 16,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "timmy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"}
response = requests.post("https://petstore.swagger.io/v2/pet", json=data_petstore)
print(response.text)



# Смена имени питомца
data_petstore = {"id": 16,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "bunny",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"}
response = requests.put("https://petstore.swagger.io/v2/pet", json=data_petstore)
print(response.text)



# Нахождение пета по айди
response = requests.get("https://petstore.swagger.io/v2/pet/16")
print(response.text)



