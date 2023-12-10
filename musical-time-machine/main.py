from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
website = response.text
soup = BeautifulSoup(website, "html.parser")
titles = soup.find_all("h3", {"id": "title-of-a-story"})
titles_no_space = [t.text.strip() for t in titles]
titles_no_head = titles_no_space[6:]
titles_no_writer = [h for h in titles_no_head if h != "Songwriter(s):"]
titles_no_producer = [h for h in titles_no_writer if h != "Producer(s):"]
title_no_promo = [h for h in titles_no_producer if h != "Imprint/Promotion Label:"]
title = title_no_promo[:10]

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
id = os.environ.get("SPOTIFY_USER_ID")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://example.com"))

song_uris = []

for song_title in title:
    results = sp.search(q=song_title, type='track')

    # Check if there are search results
    if results['tracks']['total'] > 0:
        # Get the URI of the first track in the search results
        song_uri = results['tracks']['items'][0]['uri']
        song_uris.append(song_uri)

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
