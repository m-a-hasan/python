import datetime
import os
import requests
import pandas as pd
import pytz


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_host = "https://api.tequila.kiwi.com"
        api_key = os.environ.get("FLIGHT_KEY")

        self.flight_header = {
            "apikey": api_key,
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip,deflate"
        }

        self.source_city = "MEL"

    def get_city_code(self):
        api_endpoint = f"{self.flight_host}/locations/dump"

        api_parameters = {
            "locale": "en-US",
            "location_types": "city",
            "limit": "7000",
            "active_only": "true"
        }

        response = requests.get(url=api_endpoint, params=api_parameters, headers=self.flight_header)
        response.raise_for_status()
        result = response.json()
        return result

    def find_lowest_price(self, city_list):
        price_list = []
        endpoint = f"{self.flight_host}/search"
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        date_f = tomorrow.strftime("%d/%m/%Y")
        six_month = pd.to_datetime(tomorrow)+pd.DateOffset(months=6)
        date_t = six_month.strftime("%d/%m/%Y")

        for destination in city_list:
            flight_param = {
                "fly_from": self.source_city,
                "fly_to": destination["IATA Code"],
                "date_from": date_f,
                "date_to": date_t,
                "sort": "price",
                "limit": "1",
                "curr": "AUD"
            }

            try:
                response = requests.get(url=endpoint, params=flight_param, headers=self.flight_header)
                response.raise_for_status()
                result = response.json()
            except:
                continue
            my_price = int(destination["Lowest Price"])
            lowest_price = int(result["data"][0]["price"])
            if lowest_price < my_price:
                timestamp = int(result['data'][0]['dTime'])
                dt = datetime.datetime.fromtimestamp(timestamp)
                # Set the timezone to Sydney
                sydney_tz = pytz.timezone('Australia/Sydney')
                sydney_time = dt.astimezone(sydney_tz)
                stopover = len(result['data'][0]["route"])
                stopover_text = ""
                if stopover > 1:
                    stopover_text = f" Flight has {stopover - 1} stop over, via {result['data'][0]['route'][0]['cityTo']} city"
                price_list.append(f"Low price alert! Only ${lowest_price} to fly from "
                                  f"{result['data'][0]['cityFrom']}-{result['data'][0]['flyFrom']} to "
                                  f"{result['data'][0]['cityTo']}-{result['data'][0]['flyTo']}, on {sydney_time}.{stopover_text}")

        return price_list
