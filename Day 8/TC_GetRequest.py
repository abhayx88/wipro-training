import requests

url="https://api.restful-api.dev/objects"

response = requests.get(url)

print(response.status_code)
print(response.json())

url="https://api.restful-api.dev/objects?id=3&id=5&id=10"

response = requests.get(url)

print(response.status_code)
print(response.json())

url="https://api.restful-api.dev/objects/7"

response = requests.get(url)

print(response.status_code)
print(response.json())

posturl="https://api.restful-api.dev/objects"

body1={"name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
       }

r1=requests.post(posturl,json=body1);
print(r1.status_code)
print(r1.json())

url = "https://api.restful-api.dev/objects/3"

payload = {
    "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())


url = "https://api.restful-api.dev/objects/7"

patch_payload = {
    "name": "Apple MacBook Pro 16 (Updated Name)"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.patch(url, json=patch_payload, headers=headers)

print(response.status_code)
print(response.json())

# DELETE request
delete_url = "https://api.restful-api.dev/objects/6"

response = requests.delete(delete_url)

print(response.status_code)
print(response.json())


