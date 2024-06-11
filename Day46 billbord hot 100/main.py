import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

travelData = input("what year you would like to travel to in YYY-MM-DD format")

res = requests.get(f"https://www.billboard.com/charts/hot-100/{travelData}")
web_page = res.text
soup = BeautifulSoup(web_page, "html.parser")
h3s = soup.find_all(name="div", class_="o-chart-results-list-row-container")

lst = [item.select_one("h3").getText().strip() for item in h3s]
print(lst)


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])