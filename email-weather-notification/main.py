import requests
import smtplib



user = "email"
password = "password"
API_KEY = "Api key"
MY_LAT = 43.405040
MY_LONG = 24.625260
UNITS = "metric"


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": UNITS,
    "appid": API_KEY
}


def email_notification(subject, text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user,
                            to_addrs=user,
                            msg=f"Subject:{subject}\n\n{text}")


response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
weather = data["list"][:4]

rain = False
thunder = False
clear = False
snow = False
cloud = False

for i in weather:
    condition = i["weather"][0]["id"]
    if condition == 800:
        clear = True
    elif 200 <= condition < 300:
        thunder = True
    elif 500 <= condition < 600:
        rain = True
    elif 600 <= condition < 700:
        snow = True
    elif condition > 800:
        cloud = True

if rain:
    email_notification(subject="Rainy Day", text="Today is going to rain")
elif thunder:
    email_notification(subject="Thunderstorm", text="Expecting heavy rains with thunders")
elif snow:
    email_notification(subject="Snow Day", text="Make a snowman in the lunch break :)")
elif cloud:
    email_notification(subject="Boring Clouds", text="Just clouds...nothing interesting")
elif clear:
    email_notification(subject="Clear Beautiful Day", text="Sunny dy :)")
