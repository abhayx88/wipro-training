import requests
from bs4 import BeautifulSoup
import json

url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)
response.raise_for_status()

try:
    soup = BeautifulSoup(response.text, "lxml")
except:
    soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.title.string if soup.title else "No Title"

hyperlinks = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        hyperlinks.append(href)

table_data = []

table = soup.find("table")
if table:
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all(["th", "td"])
        row_data = [cell.text.strip() for cell in cells]
        table_data.append(row_data)

extracted_data = {
    "page_title": page_title,
    "hyperlinks": hyperlinks,
    "table_data": table_data
}

json_data = json.dumps(extracted_data, indent=4)

with open("extracted_data.json", "w", encoding="utf-8") as file:
    file.write(json_data)

print("Data extracted and saved successfully to extracted_data.json")
