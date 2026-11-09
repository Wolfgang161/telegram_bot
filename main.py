# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import requests
import os

# import os and use it to get the Github repository secrets
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_CHATID = os.environ.get("BOT_CHATID")
MY_LAT = os.environ.get("MY_LAT") 
MY_LON = os.environ.get("MY_LON") 

parameters = {
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":api_key,
    "cnt":4,
}

def send_telegram(telegram_message):
    send_text = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage?chat_id=" + BOT_CHATID + "&parse_mode=Markdown&text=" + telegram_message
    response = requests.get(send_text)
    print(response)

weather_api = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params= parameters)
weather_api.raise_for_status()
weather_data = weather_api.json()

will_it_rain = False
for x in range(0,len(weather_data["list"])):
    if weather_data["list"][x]["weather"][0]["id"] < 700:
        will_it_rain = True
if will_it_rain:
    send_telegram("It will rain. Bring an umbrella")
else:
    send_telegram("It will not rain. No need to bring an umbrella")
