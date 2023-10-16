import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        sheet_endpoint = "https://api.sheety.co/halihalibotedemofabang"
        response = requests.get(url=sheet_endpoint)
        response.raise_for_status()
        self.data = response.json()["prices"]
        BEARER_TOKEN = "fdsljflejlajgjela;gueio;ata;hja;jgrwetwtwojg"
        self.bearer_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


    def data_put(self, data, response):
        OBJECT_ID = data["id"]
        put_endpoint = f"https://api.sheety.co/halihalibotedemofabang/flightDeals/prices/{OBJECT_ID}"
        sheet_inputs = {
            "price": {
                "iataCode": response,
            },
        }

        sheet_response = requests.put(url=put_endpoint, json=sheet_inputs, headers=self.bearer_headers)
        sheet_response.raise_for_status()
        print(sheet_response.text)