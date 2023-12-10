from twilio.rest import Client
import os
import requests

API_KEY = os.environ.get("WEATHER_API_KEY")
LATITUDE = -37.722630
LONGITUDE = 144.768120
URL = "https://api.openweathermap.org/data/2.5/onecall"
ACCOUNT_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
FROM_NUMBER = os.environ.get("RAIN_ALERT_FROM_NUMBER")
TO_NUMBER = os.environ.get("RAIN_ALERT_TO_NUMBER")

parameter = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(URL, params=parameter)
response.raise_for_status()
status = response.status_code
weather_data = response.json()
print(status)
print(weather_data)

hourly_data = weather_data["hourly"]
recent_hourly_data = hourly_data[:12]

weather_codes = [hourly_details["weather"][0]["id"] for hourly_details in recent_hourly_data if hourly_details["weather"][0]["id"] < 700]

if len(weather_codes) > 0:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
      body="It's going to rain today, remember to bring an ☔️",
      from_=FROM_NUMBER,
      to=TO_NUMBER
    )

    print(message.status)