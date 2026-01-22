import requests
import json

url = "https://api.restful-api.dev/objects"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-REST-API-Program"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    extracted_data = []
    for item in data:
        extracted_data.append({
            "id": item["id"],
            "name": item["name"],
            "data": item["data"]
        })

    with open("products.json", "w") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data successfully saved")

except requests.exceptions.HTTPError as e:
    print("HTTP Error occurred:", e)

except requests.exceptions.RequestException as e:
    print("Request Error occurred:", e)
