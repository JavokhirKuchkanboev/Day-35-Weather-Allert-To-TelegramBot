import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
message = "Zo'ntik esdan chiqmasin, bugub yomg'ir yog'ishi mumkin ☔"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

MY_LAT = 40.787378
MY_LNG = 72.509820

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "cnt": 4,
    "appid": "e55b2f4c0082e62b643c2cbb1e1d455a"

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()

condition = [day["weather"][0]["id"] for day in data["list"]]



will_rain = False

for con in condition:
    if con < 700:
        will_rain = True

if will_rain:
    response = requests.post(url, data=payload)
    response.raise_for_status()