from twilio.rest import Client
import requests

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_key = ""
account_sid = ""
auth_token = ""

LATITUDE = 19.701870
LONGITUDE = -101.192340

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for i in range(12):
    condition_code = data["hourly"][i]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella ",
                        from_='+12187890977',
                        to='+524431054555'
                    )

print(message.status)
