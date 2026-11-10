import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("./.env")


# import os and use it to get the Github repository secrets
WEATHER_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_CHATID = os.environ.get("BOT_CHATID")
MY_LAT = os.environ.get("MY_LAT") 
MY_LON = os.environ.get("MY_LON") 

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": WEATHER_API_KEY,
    "cnt": 4,
}

def send_telegram(telegram_message):
    send_text = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage?chat_id=" + BOT_CHATID + "&parse_mode=Markdown&text=" + telegram_message
    response_tele = requests.get(send_text)
    response_tele.raise_for_status()

weather_api = requests.get(url=WEATHER_Endpoint, params=parameters)
weather_api.raise_for_status()
weather_data = weather_api.json()

timestamps = []
date_format = "%Y-%m-%d %H:%M:%S"

weekdaylist = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitrag", "Samstag", "Sonntag"]

symbol=""
for x in range (0,4):
    timestamps.append(weather_data["list"][x]["dt_txt"])
    if 200 < weather_data["list"][x]["weather"][0]["id"] <300:
        symbol += "⛈"
    elif 300 < weather_data["list"][x]["weather"][0]["id"] <600:
        symbol += "🌧"
    elif 600 < weather_data["list"][x]["weather"][0]["id"] <700:
        symbol += "🌨"
    elif weather_data["list"][x]["weather"][0]["id"]==800:
        symbol += "☀"
    elif weather_data["list"][x]["weather"][0]["id"]>800:
        symbol += "☁"

date = [datetime.strptime(x,date_format) for x in timestamps]
send_telegram(f"Guten Morgen Jana! 🦾🦾🦾\nWetter {weekdaylist[datetime.now().weekday()]}, {date[0].day}.{date[0].month}.{date[0].year}\n{date[0].hour} Uhr: {round(weather_data["list"][0]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][0]["weather"][0]["main"]}: {weather_data["list"][0]["weather"][0]["description"]}\n{date[1].hour} Uhr: {round(weather_data["list"][1]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][1]["weather"][0]["main"]}: {weather_data["list"][1]["weather"][0]["description"]}\n{date[2].hour} Uhr: {round(weather_data["list"][2]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][2]["weather"][0]["main"]}: {weather_data["list"][2]["weather"][0]["description"]}\n{date[3].hour} Uhr: {round(weather_data["list"][3]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][3]["weather"][0]["main"]}: {weather_data["list"][3]["weather"][0]["description"]}\n-JanaBot 💚{symbol}")

