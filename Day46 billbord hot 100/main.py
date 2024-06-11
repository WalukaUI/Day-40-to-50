import requests
from bs4 import BeautifulSoup

travelData = input("what year you would like to travel to in YYY-MM-DD format")

res = requests.get(f"https://www.billboard.com/charts/hot-100/{travelData}")
web_page = res.text
soup = BeautifulSoup(web_page, "html.parser")
h3s = soup.find_all(name="div", class_="o-chart-results-list-row-container")

lst = [item.select_one("h3").getText().strip() for item in h3s]
print(lst)

