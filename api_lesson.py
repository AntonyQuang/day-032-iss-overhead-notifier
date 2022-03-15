import requests
from datetime import datetime

MY_LAT = 51.376163
MY_LON = -0.098234

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(data)

time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)
