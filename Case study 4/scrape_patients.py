import requests
from bs4 import BeautifulSoup

response = requests.get("http://127.0.0.1:5000/patients")
soup = BeautifulSoup(response.text, "lxml")

rows = soup.find_all("tr")[1:]  # skip header

for row in rows:
    cols = row.find_all("td")
    print(
        "Name:", cols[0].text,
        "Age:", cols[1].text,
        "Disease:", cols[2].text,
        "Doctor:", cols[3].text
    )
