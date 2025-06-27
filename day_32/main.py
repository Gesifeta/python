##################### Extra Hard Starting Project ######################
import smtplib
import random
import pandas as pd
import os
import datetime as dt

# set up the email connection
password ="ypcr nvek fjph qaoq"
file_dir = os.path.dirname(__file__)

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
def check_birthday():
    try:
        now = dt.datetime.now()
        birth_days_data = pd.read_csv(f"{file_dir}/birthdays.csv")
    except FileNotFoundError:
        birth_days_data ="No birthday data found"
    else:
        month = now.month
        day = now.day
        for birth_day in birth_days_data.values:
            if birth_day[3] == month and birth_day[4] == day:
                my_birth_day_wish = pick_letters()
                my_letter = my_birth_day_wish.replace("[NAME]",birth_day[0])
                sendMail(birth_day[1],f"subject:Birthday Wishes\n\n{my_letter}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_letters():
    try:
        random_letter = random.randint(1,4)
        with open(f"{file_dir}/letter_templates/letter_{random_letter}.txt","r") as letter_file:
            letter = letter_file.read()
    except FileNotFoundError:
        letter = "Happy birth day"
        return letter
    else:
        return letter
# 4. Send the letter generated in step 3 to that person's email address.
def sendMail(email,message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("adamgemechu@gmail.com",password)
        connection.sendmail(from_addr="adamgemechu@gmail.com",to_addrs=email,msg=message)

check_birthday()




