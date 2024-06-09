from bs4 import BeautifulSoup
import requests

res =requests.get("https://news.ycombinator.com/news")
web_page = res.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

for tag in articles:
    print(tag.select_one("a").getText())

#
# with open("website.html", encoding='utf-8')as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# tags = soup.find_all(name="a")
# for tag in tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# classes= soup.find(name="h3", class_="heading")
# print(classes)
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# name = soup.select_one(selector="#name")
# print(name)
#
# all_classes = soup.select(selector=".heading")
# print(all_classes)