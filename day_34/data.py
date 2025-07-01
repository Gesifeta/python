import requests
def get_quizes():    
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    data =  response.json()["results"]
    return data