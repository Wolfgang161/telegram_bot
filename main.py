# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_2EMAIL = os.environ.get("MY_2EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today= dt.datetime.now()
day = today.day
month = today.month

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dic = pandas.DataFrame.to_dict(birthdays,orient="records")

for entry in birthdays_dic:
    if month == entry["month"] and day == entry["day"]:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            chosen_letter = letter.read()
            modified_letter = chosen_letter.replace("[NAME]",entry["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_2EMAIL,
                msg=f"Subject:Geburtstag: {entry["name"]}\n\n{modified_letter}"
            )
