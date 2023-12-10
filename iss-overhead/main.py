import requests
from datetime import datetime
import smtplib

MY_LAT = -37.722630 # Your latitude
MY_LONG = 144.768120 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow().hour


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5
        and sunset <= time_now <= sunrise):
    from_email = "abid.mail.test@gmail.com"
    to_email = "abid_mail_test@yahoo.com"
    from_emil_pass = "nytw bcus txbz kjww"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_emil_pass)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg="Subject:Look up!\n\nYou might catch the satellite passing by"
        )


