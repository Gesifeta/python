import requests
import os
import datetime

from api import stock_api_key, news_api_key

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key,
    "outputsize":"compact"
}
dt = datetime.datetime
today = dt.now().strftime("%D").split("/")
today_day = today[1]

# Get yesterday's day by removing the today, and inserting today minus one
today.remove(today_day)
if  0 < int(today_day) - 1 < 10:
    today.insert(1,"0"+ str(int(today_day)-1))
else:
    today.insert(1,str(int(today_day)-1))
yesterday = "/".join(today)

# Get yesterday's day by removing the today, and inserting today minus two
today.remove(today[1])
if  0 < int(today_day) - 2 < 10:
    today.insert(1,"0" + str(int(today_day)-2))
else:
    today.insert(1,str(int(today_day)-2))
before_yesterday = "/".join(today)
print("Yesterday",yesterday)
print("Before Yesterday",before_yesterday)





## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# response = requests.get(url="https://www.alphavantage.co/query",params=stock_params)
# response.raise_for_status()
# data = response.json()["Time Series (Daily)"]
# print(dt.now().strftime("%D"))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

