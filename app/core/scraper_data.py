import requests
from bs4 import BeautifulSoup


url = "https://www.mlb.com/es/yankees/schedule/2025-07"

response = requests.get(url)
html = response.text.strip()

sopa = BeautifulSoup(html, "html.parser")
tabla = sopa.find("tr", {"class": "primary-row-tr"})
print(tabla)