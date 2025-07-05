import requests
from api import api_key

params ={
    "lat":9.181256,
    "lon":38.7593782,
    "appid":api_key,
    "cnt":5
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast",params=params)
response.raise_for_status()
data = response.json()["list"]
for rain in data:
    if rain["weather"][0]["id"] < 600:
        print("It will rain and bring umberella")