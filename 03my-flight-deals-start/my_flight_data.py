from datetime import datetime, timedelta
import requests

today = datetime.now()
tomorrow = today + timedelta(days=1)
tomorrow_formatted = tomorrow.strftime("%d/%m/%Y")

six_months_later = today + timedelta(days=180)
six_months_later_formatted = six_months_later.strftime("%d/%m/%Y")

class FlightData:
    #This class is responsible for structuring the flight data.
    def get_lowest_price(self, sheet_data):
        for row in sheet_data:
            TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
            TEQUILA_API_KEY = "halihalibotedemofabang"
            search_endpoint = f"{TEQUILA_ENDPOINT}/search"
            headers = {
                "apikey": TEQUILA_API_KEY
            }
            search = {
                "fly_from": "BJS",
                "fly_to": row["iataCode"],
                "date_from": tomorrow_formatted,
                "date_to": six_months_later_formatted,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
            }

            response = requests.get(url=search_endpoint, headers=headers, params=search)
            response.raise_for_status()
            prices = []
            for data in response.json()["data"]:
                prices.append(data["price"])
                lowest_price = min(prices)
            print(lowest_price)