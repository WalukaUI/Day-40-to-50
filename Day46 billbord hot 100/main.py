import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

travelData = input("what year you would like to travel to in YYY-MM-DD format")

res = requests.get(f"https://www.billboard.com/charts/hot-100/{travelData}")
web_page = res.text
soup = BeautifulSoup(web_page, "html.parser")
h3s = soup.find_all(name="div", class_="o-chart-results-list-row-container")

lst = [item.select_one("h3").getText().strip() for item in h3s]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="5xxxxxxxxxxxxxxxxxx",
        client_secret="8xxxxxxxxxxxxxx",
        show_dialog=True,
        cache_path="token.txt",
        username="waluka",
    )
)
user_id = sp.current_user()["id"]


