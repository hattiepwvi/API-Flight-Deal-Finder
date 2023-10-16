import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data):
        flight_search_endpoint = f"https://api.tequila.kiwi.com/locations/query"
        parameters = {
            "apikey": "halihalibotedemofabang",
            "term": data["iataCode"]
        }
        self.response = requests.get(url=flight_search_endpoint, params=parameters)


