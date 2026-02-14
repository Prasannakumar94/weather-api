import requests

API_KEY = "88aa0b8e54af067b2b71170671e3972f"

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
