import vonage

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, flight):
        client = vonage.Client(key="halihalibotedemofabang", secret="halihalibotedemofabang")
        sms = vonage.Sms(client)
        responseData = sms.send_message(
            {
                "from": "Vonage APIs",
                "to": "86halihalibotedemofabang",
                "text": f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}",
            }
        )
        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
