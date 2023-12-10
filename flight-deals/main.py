from data_manager import DataManager
from flight_search import FlightSearch
from twilio.rest import Client
import os

spreadsheet = DataManager()
flight_search = FlightSearch()


def user_onboard():
    print("Welcome to Abid's flight club.\nWe will find the best flight deal and email you.")
    fname = input("What is your first name?\n")
    lname = input("What is your last name?\n")
    email = input("What is your email?\n")
    print("Thanks for joining the club!")
    spreadsheet.insert_user(fname, lname, email)

def send_message(msg):
    ACCOUNT_SID = os.environ.get("TWILIO_SID")
    AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
    FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
    TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for m in msg:
        message = client.messages.create(
            body=m,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )

        print(message.status)

def populate_city(details, to_populate):
    for p in to_populate:
        for d in details["results"]:
            if p["City"].lower() == d["City"].lower():
                p["id"] = d["rowIndex"]
                break
    return to_populate


def get_city_codes(missing):
    codes = []
    city_codes = flight_search.get_city_code()
    for city in missing:
        for loc in city_codes["locations"]:
            if city.lower() == loc["name"].lower():
                flight = {
                    "City": city,
                    "IATA Code": loc["code"]
                }
                codes.append(flight)
                break
    return codes


user_onboard()

spreadsheet_data = spreadsheet.check_city_code()
# spreadsheet_data = {'results': [{'City': 'Paris', 'IATA Code': 'PAR', 'Lowest Price': '54', 'rowIndex': 2}, {'City': 'Berlin', 'IATA Code': 'BER', 'Lowest Price': '42', 'rowIndex': 3}, {'City': 'Tokyo', 'IATA Code': 'TYO', 'Lowest Price': '485', 'rowIndex': 4}, {'City': 'Sydney', 'IATA Code': 'SYD', 'Lowest Price': '551', 'rowIndex': 5}, {'City': 'Istanbul', 'IATA Code': 'IST', 'Lowest Price': '95', 'rowIndex': 6}, {'City': 'Kuala Lumpur', 'IATA Code': 'KUL', 'Lowest Price': '414', 'rowIndex': 7}, {'City': 'New York', 'IATA Code': 'NYC', 'Lowest Price': '240', 'rowIndex': 8}, {'City': 'San Francisco', 'IATA Code': 'SFO', 'Lowest Price': '260', 'rowIndex': 9}, {'City': 'Cape Town', 'IATA Code': 'CPT', 'Lowest Price': '378', 'rowIndex': 10}], 'hasNextPage': False}

missing_city_code = [city["City"] for city in spreadsheet_data["results"] if len(city["IATA Code"]) == 0]

if len(missing_city_code) > 0:
    city_code_list = get_city_codes(missing_city_code)
    city_list = populate_city(spreadsheet_data, city_code_list)
    spreadsheet.send_city_codes(city_list)

lowest_prices = flight_search.find_lowest_price(spreadsheet_data["results"])
print(lowest_prices)
#
# if len(lowest_prices) > 0:
#     send_message(lowest_prices)