from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/imworthitaowu/flightDealsUsers/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/imworthitaowu/flightDealsUsers/users"
BEARER = "imworthitaowu"
headers = {
      "Authorization": f"Bearer {BEARER}",
      "Content-Type": "application/json",
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=headers,
                json=new_data,
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

