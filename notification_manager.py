import vonage
import smtplib


VONAGE_KEY = "imworthitaowu"
VONAGE_SECRET = "imworthitaowu"
TEL = "imworthitaowu"
my_email = "imworthitaowu@gmail.com"
password = "imworthitaowu"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        client = vonage.Client(key=VONAGE_KEY, secret=VONAGE_SECRET)
        self.sms = vonage.Sms(client)

    def send_sms(self, message):
        response_data = self.sms.send_message(
            {
                "from": "Vonage APIs",
                "to": TEL,
                "text": message,
            }
        )
        if response_data["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {response_data['messages'][0]['error-text']}")

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
