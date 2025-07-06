import requests
import os
import datetime

from api import stock_api_key, news_api_key

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


dt = datetime.datetime
today = str(dt.now()).split(" ")[0].split("-")

today_day = today[2]

# Get yesterday's day by removing the today, and inserting today minus one
today.remove(today_day)
if  0 < int(today_day) - 3 < 10:
    today.insert(2,"0"+ str(int(today_day)-3))
else:
    today.insert(2,str(int(today_day)-3))
yesterday = "-".join(today)

# Get yesterday's day by removing the today, and inserting today minus two
today.remove(today[2])
if  0 < int(today_day) - 4 < 10:
    today.insert(2,"0" + str(int(today_day)-4))
else:
    today.insert(2,str(int(today_day)-4))
before_yesterday = "-".join(today)


stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key,
    "outputsize":"compact"
}
news_params= {
"q":COMPANY_NAME,
"from":before_yesterday,
"to":yesterday,
"sortBy":"popularity",
"apiKey":news_api_key
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url="https://www.alphavantage.co/query",params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_price_movement = ((float(stock_data[before_yesterday]["4. close"]) - float(stock_data[yesterday]["4. close"]))/float(stock_data[before_yesterday]["4. close"]))*100

news_response =requests.get(url="https://newsapi.org/v2/top-headlines/",params= news_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"][:4]

if abs(stock_price_movement) > .05:
    print(f"{STOCK} : moved {stock_price_movement}")
    for headline in news_data:
        print(f"Headlines [{headline["source"]["name"]}], By {headline["author"]} ")
        print(headline["title"])
  
else:
    print("No major changes")

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

