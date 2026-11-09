import os
import requests


# import os and use it to get the Github repository secrets
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

#def send_telegram(telegram_message):
#    send_text = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage?chat_id=" + BOT_CHATID + "&parse_mode=Markdown&text=" + telegram_message
#    #response = requests.get(send_text)
#    #print(response)

weather_api = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params= parameters)
weather_api.raise_for_status()
weather_data = weather_api.json()

will_it_rain = False

for x in range(0,len(weather_data["list"])):
    if weather_data["list"][x]["weather"][0]["id"] < 700:
        will_it_rain = True
#if will_it_rain:
#    send_telegram("It will rain today. Remember to bring an umbrella ☔")
#else:
#    send_telegram("It will not rain. No need to bring an umbrella")
