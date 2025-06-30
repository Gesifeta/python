import requests

MY_LAT = 9.183420
MY_LONG = 38.759521

params = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formated":True
}

def get_sunrise():
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=params)
    response.raise_for_status()
    data = response.json()
    print(data)
get_sunrise()