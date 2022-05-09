import json
import os
from datetime import date, timedelta

import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError

from extract import json_extract

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
DEFAULT_SESSION_DURATION_DAYS = 7


class HotelSession:
    def __init__(
        self, location=None, destination_id=None, currency="EUR", querystring=None
    ):
        self.location = location
        self.destination_id = destination_id
        self.currency = currency
        self.querystring = querystring

    def set_location_and_destination_id(self, location):

        url = "https://hotels4.p.rapidapi.com/locations/v2/search"
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "hotels4.p.rapidapi.com",
        }
        querystring = {"query": location, "currency": self.currency}

        success, data = self._send_request(url, headers, querystring)

        if not success:
            return data, None

        destination_id = data["suggestions"][0]["entities"][0]["destinationId"]
        name = data["suggestions"][0]["entities"][0]["name"]

        self.location = name
        self.destination_id = destination_id
        return name, destination_id

    def get_hotels_for_destination_id(self):
        if not self.destination_id:
            return "Please provide location for hotels to be found!"

        url = "https://hotels4.p.rapidapi.com/properties/list"
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "hotels4.p.rapidapi.com",
        }

        # TODO: Add params validation
        # mm/dd/y
        today = date.today()
        checkIn = today.strftime("%Y-%m-%d")
        checkOut = (today + timedelta(days=DEFAULT_SESSION_DURATION_DAYS)).strftime(
            "%Y-%m-%d"
        )
        print(f"{checkIn}, {checkOut}")
        querystring = {
            "destinationId": self.destination_id,
            "pageNumber": "1",
            "pageSize": "25",
            "checkIn": checkIn,
            "checkOut": checkOut,
            "currency": self.currency,
        }
        if self.querystring:
            for key, value in self.querystring.items():
                querystring[key] = value

        success, data = self._send_request(url, headers, querystring)

        if not success:
            return data

        return self._prepare_hotels_response(data)

    def add_to_querysting(self, parameter, value):
        if not self.querystring:
            self.querystring = {}

        self.querystring.update({parameter: str(value)})

        return str(self.querystring)

    def _send_request(self, url, headers, querystring):
        try:
            print(f"request url={url},\nquerystring={querystring}")
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
        except HTTPError as http_err:
            return False, f"HTTP error occurred: {http_err}"
        except Exception as err:
            return False, f"Other error occurred: {err}"
        else:
            return True, json.loads(response.text)

    def _prepare_hotels_response(self, data):
        data = data["data"]["body"]

        if data:
            new_message = "Hotels info response:\n"

            name = json_extract(data, "value")
            if name:
                new_message += f"Hotels in {name}\n"

            total_count = json_extract(data, "totalCount")

            if total_count:
                new_message += f"Found {total_count} hotels\n"

            results = json_extract(data, "results", True)

            if results and results[0]:
                new_message += f"Hotels:\n"
                for num, hotel in enumerate(results, 1):
                    new_message += f"{num}. {hotel['name']}\n"

        else:
            new_message = "No results found"
        return new_message
