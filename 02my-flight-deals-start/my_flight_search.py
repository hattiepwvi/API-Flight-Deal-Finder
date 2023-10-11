import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "halihalibotedemofabang"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.

        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        parameters = {
            "term": city_name
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=parameters, headers=headers)
        # row["iataCode"] = response.json()["locations"][0]["code"]

        code = response.json()["locations"][0]["code"]
        return code


