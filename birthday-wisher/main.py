import pandas as pd
import datetime as dt
import random
import smtplib


# ---------------------- Extra Hard Starting Project ------------------------ #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
birthday_list = birthdays.to_dict(orient="records")

current_date = dt.datetime.now()
this_day = current_date.day
this_month = current_date.month

wish_list = [people for people in birthday_list if this_day == people["day"] and this_month == people["month"]]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
# person's actual name from birthdays.csv

from_email = "abid.mail.test@gmail.com"
from_emil_pass = "nytw bcus txbz kjww"

for people in wish_list:
    file_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{file_number}.txt") as f:
        letter = f.read().replace("[NAME]", people["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_email, password=from_emil_pass)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=people["email"],
                msg=f"Subject:Happy birthday!\n\n{letter}"
            )
