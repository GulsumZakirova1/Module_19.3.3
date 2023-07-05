import requests

# GET запрос
status = "available"

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={"accept":"application/json"})

print('GET,', res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# POST запрос

url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept':'application/json',
    'Content-Type':'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post(url, headers=headers, json=data)

print('POST,', res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# PUT запрос

url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept':'application/json',
    'Content-Type':'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "mew",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.put(url, headers=headers, json=data)

print('PUT,', res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# DELETE запрос

pet_Id = "1"
headers = {
    "accept":"application/json"
}
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_Id}", headers=headers)

print('DELETE,', res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

