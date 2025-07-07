
import requests
from .config import OPENWEATHER_API_KEY

def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
