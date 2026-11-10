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

try:
    weather_api = requests.get(url=WEATHER_Endpoint, params=parameters)
    weather_api.raise_for_status()
except:
    send_telegram("There is a problem with the openweathermap request.")
else:
    weather_data = weather_api.json()
    timestamp_0 = weather_data["list"][0]["dt_txt"]
    timestamp_1 = weather_data["list"][1]["dt_txt"]
    timestamp_2 = weather_data["list"][2]["dt_txt"]
    timestamp_3 = weather_data["list"][3]["dt_txt"]
    f_0 = "%Y-%m-%d %H:%M:%S"
    date_0 = datetime.strptime(timestamp_0,f_0)
    date_1 = datetime.strptime(timestamp_1,f_0)
    date_2 = datetime.strptime(timestamp_2,f_0)
    date_3 = datetime.strptime(timestamp_3,f_0)

    send_telegram(f"#-Wettervorhersage vom {date_0.day}.{date_0.month}.{date_0.year}-#\n"
      f"{date_0.hour} Uhr: {round(weather_data["list"][0]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][0]["weather"][0]["main"]}: {weather_data["list"][0]["weather"][0]["description"]}\n"
      f"{date_1.hour} Uhr: {round(weather_data["list"][1]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][1]["weather"][0]["main"]}: {weather_data["list"][1]["weather"][0]["description"]}\n"
      f"{date_2.hour} Uhr: {round(weather_data["list"][2]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][2]["weather"][0]["main"]}: {weather_data["list"][2]["weather"][0]["description"]}\n"
      f"{date_3.hour} Uhr: {round(weather_data["list"][3]["main"]["temp"] - 273.15,0)}°C {weather_data["list"][3]["weather"][0]["main"]}: {weather_data["list"][3]["weather"][0]["description"]}\n"
      f"Erstellt vom Jana_Bot um {datetime.now().time().hour} Uhr")
