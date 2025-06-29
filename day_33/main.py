import requests

responses = requests.get(url="http://api.open-notify.org/iss-now.json")
responses.raise_for_status()
data = responses.json()
print(data)