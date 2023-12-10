from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h3", {"class": "listicleItem_listicle-item__title__hW_Kn"})
title_head = [t.text for t in titles]

with open("movie_list.txt", "w") as file:
    for item in reversed(title_head):
        file.write(item + "\n")