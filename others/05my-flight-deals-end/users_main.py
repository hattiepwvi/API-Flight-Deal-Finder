import requests

USER_ENDPOINT = "https://api.sheety.co/imworthitaowu/flightDealsUsers/users"
BEARER = "imworthitaowu"
email_exists = False

print(
    "Welcome to Eta's Flight Club!\n We find best flight deals and email you!\n"
)
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
email = input("Type your email ")

headers = {
            "Authorization": f"Bearer {BEARER}",
            "Content-Type": "application/json",
        }

response = requests.get(url=USER_ENDPOINT, headers=headers)
users = response.json()["users"]
print(response.json())
print(response.json()["users"])

for user in users:
    if email == user["email"]:
        email_exists = True
        break
if not email_exists:
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }
    new_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    response = requests.post(url=USER_ENDPOINT, headers=headers, json=new_data)
    print("Success, your email has been added")
else:
    print("You have subcribed our services.")