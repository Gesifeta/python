import requests
from api import api_key

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat=9.1812561&lon=38.7593782&appid={api_key}")
response.raise_for_status()
data = response.json()

print(data)
print(response.status_code)