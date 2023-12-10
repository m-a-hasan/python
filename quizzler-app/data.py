import requests

AMOUNT = 10
TYPE = "boolean"
TRIVIA_URL = "https://opentdb.com/api.php"

parameter = {
    "amount": AMOUNT,
    "type": TYPE
}

response = requests.get(TRIVIA_URL, params=parameter)
response.raise_for_status()
question_data = response.json()["results"]

