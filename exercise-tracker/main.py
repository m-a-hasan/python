import requests
import os
import datetime

GENDER = "MALE"
WEIGHT_KG = "68"
HEIGHT = "168.0" #entered random height in cm
AGE = "34"

APP_ID = os.environ.get("NUTRITIONIX_ID")
APP_KEY = os.environ.get("NUTRITIONIX_KEY")
SHEETY_URL = os.environ.get("SHEETY_URL")
SHEETY_TOKEN = os.environ.get("SHEETY_KEY")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# exercise_input = input("Tell me which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': APP_KEY,
    "Content-Type": "application/json"
}

# parameters = {
#     'query': exercise_input,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT,
#     "age": AGE,
# }

# Ran 5k and cycled for 20 minutes.

# response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=header, verify=False)
# response.raise_for_status()
# result = response.json()

result = {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 20.01, 'met': 9.8, 'nf_calories': 222.24, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}, {'tag_id': 100, 'user_input': 'walked', 'duration_min': 37.28, 'met': 3.5, 'nf_calories': 147.88, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 17190, 'name': 'walking', 'description': None, 'benefits': None}]}

sheety_endpoint = f"https://api.sheety.co/{SHEETY_URL}/myWorkouts/workouts"

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

print()
print()

for items in result["exercises"]:
    sheety_parameters = {
      "workout": {
        "date": datetime.datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.datetime.now().strftime("%H:%M:00"),
        "exercise": items["name"].title(),
        "duration": items["duration_min"],
        "calories": items["nf_calories"]
      }
    }

    response = requests.post(sheety_endpoint, json=sheety_parameters, headers=sheety_header)
    print(response.text)