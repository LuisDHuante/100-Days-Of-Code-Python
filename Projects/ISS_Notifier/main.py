import smtplib
import requests
from datetime import datetime
import time

#Solution: https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84


EMAIL_SENDER = "deuteronomy35@gmail.com"
EMAIL_DESTINATION = "luisdhuante@gmail.com"
MY_PASSWORD = "rYLe3qsC2A"
MY_LAT = 19.705950  # Your latitude
MY_LONG = -101.194984  # Your longitude


def iss_is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if iss_is_above() and is_night():
        time.sleep(60)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL_SENDER, MY_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=EMAIL_DESTINATION,
            msg="Subject: ISS Overhead\n\n The ISS is above you in the sky. Look up.")
