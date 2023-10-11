#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from my_data_manager import DataManager
from my_flight_search import FlightSearch
import requests
sheet_data = DataManager()

for data in sheet_data.data:
    flight_search = FlightSearch(data)
    if data["iataCode"] == "":
        response = "TESTING"
        print(response)
    else:

        response = flight_search.response.json()

    sheet_data.data_put(data, response)





