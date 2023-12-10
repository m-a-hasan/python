from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

# anchor_tags = soup.findAll("a")
# for link in anchor_tags:
#     print(link)

span = soup.find("span", {"class": "titleline"})
anchor_text = span.find("a").text
anchor_value = span.find("a")["href"]
score = soup.find("span", {"class": "score"}).text
print(anchor_value)
print(anchor_text)
print(score)
