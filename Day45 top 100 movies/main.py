import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

res = requests.get(URL)
webpage = res.text

soup = BeautifulSoup(webpage, "html.parser")
h3_list = soup.find_all(name="h3", class_="title")
all_movies = [h3.getText() for h3 in h3_list][::-1]
print(all_movies)

with open("movie.txt", mode="w")as file:
    for movie in all_movies:
        file.write(f"{movie}\n")
