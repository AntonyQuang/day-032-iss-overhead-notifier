import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.376163   # Your latitude
MY_LONG = -0.098234   # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

senders_email = "antony.quang@yahoo.com"
senders_password = "bwurmbfgsgkbpsly"


def position_checker():
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5:
        return iss_longitude - 5 <= MY_LONG < iss_longitude + 5
    else:
        return False


def send_mail():
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=senders_email, password=senders_password)
        connection.sendmail(from_addr=senders_email, to_addrs="antony.quang@googlemail.com",
                            msg=f"Subject:Look up!\n\nThe Internation Space Station is in the sky!")


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if sunrise <= time_now.hour <= sunset:
        return True


while True:
    time.sleep(60)
    if position_checker() and is_night():
        send_mail()


# BONUS: run the code every 60 seconds.
