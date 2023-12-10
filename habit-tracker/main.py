import os
import requests
import datetime

USER_TOKEN = os.environ.get("PIXELA_TOKEN")
USER_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "abid"
GRAPH_ID = "abid-graph"

GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
UPDATE_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20231030"

user_param = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(USER_ENDPOINT, json=user_param)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "My Exercise Graph",
    "unit": "minutes1`",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

# response = requests.post(GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

today = datetime.datetime.now().strftime("%Y%m%d")

pixel_param = {
    "date": today,
    "quantity": input("How many minutes have you exercised today? "),
}

response = requests.post(PIXEL_ENDPOINT, json=pixel_param, headers=headers)
print(response.text)

update_param = {
    "quantity": "10",
}

# response = requests.put(UPDATE_ENDPOINT, json=update_param, headers=headers)
# print(response.text)

# response = requests.delete(UPDATE_ENDPOINT, headers=headers)
# print(response.text)