import requests

geturl = "http://127.0.0.1:5000/users"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Client"

}
response = requests.get(geturl, headers=headers, timeout=10)

print("get status code", response.status_code)
print(response.json())

posturl = "http://127.0.0.1:5000/users"

body1 = {
    "name": "leena"
}

r1 = requests.post(posturl, json=body1);
print("post status code", r1.status_code)
print(r1.json())
