import vonage

VONAGE_KEY = "halihalibotedemofabang"
VONAGE_SECRET = "halihalibotedemofabang"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        client = vonage.Client(key=VONAGE_KEY, secret=VONAGE_SECRET)
        self.sms = vonage.Sms(client)

    def send_sms(self, message):
        response_data = self.sms.send_message(
            {
                "from": "Vonage APIs",
                "to": "86xxx",
                "text": message,
            }
        )
        if response_data["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {response_data['messages'][0]['error-text']}")
