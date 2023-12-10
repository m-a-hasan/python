import requests
from datetime import datetime

MELB_LAT = -37.813629
MELB_LONG = 144.963058
SUNRISE_SUNSET_URL = "https://api.sunrise-sunset.org/json"

parameter = {
    "lat": MELB_LAT,
    "lng": MELB_LONG,
    "formatted": 0
}

response = requests.get(SUNRISE_SUNSET_URL, params=parameter)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
print(sunrise)

time_now = datetime.now()
print(time_now)