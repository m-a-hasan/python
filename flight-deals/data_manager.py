import requests
import os
import datetime


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheetson_price_url = "https://api.sheetson.com/v2/sheets/prices"
        self.sheetson_user_url = "https://api.sheetson.com/v2/sheets/users"
        self.sheetson_token = os.environ.get("SHEETSON_KEY")
        self.sheetson_id = os.environ.get("FLIGHT_SHEET_URL")

        self.sheetson_header = {
            "Authorization": f"Bearer {self.sheetson_token}",
            "X-Spreadsheet-Id": self.sheetson_id,
            "Content-Type": "application/json"
        }

    def check_city_code(self):
        params = {
            "apiKey": self.sheetson_token,
            "spreadsheetId": self.sheetson_id,
        }

        response = requests.get(self.sheetson_price_url, params=params)
        response.raise_for_status()
        result = response.json()
        return result

    def send_city_codes(self, iata_list):
        for item in iata_list:
            sheetson_endpoint = f"{self.sheetson_price_url}/{item['id']}"

            parameters = {
                "rowIndex": item["id"],
                "IATA Code": item["IATA Code"]
            }

            response = requests.put(sheetson_endpoint, json=parameters, headers=self.sheetson_header)
            response.raise_for_status()
            print(response.text)

    def insert_user(self, fname, lname, email):
        parameters = {
            "First Name": fname,
            "Last Name": lname,
            "Email": email
        }

        response = requests.post(self.sheetson_user_url, json=parameters, headers=self.sheetson_header)
        response.raise_for_status()
        print(response.text)