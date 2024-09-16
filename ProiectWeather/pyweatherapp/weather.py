# weather.py
import requests
from pyweatherapp.config import API_KEY


def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return {"error": "Orașul nu a fost găsit"}

def display_weather(city):
    weather = get_weather(city)
    if "error" not in weather:
        print(f"Vremea în {weather['city']}:")
        print(f"Temperatura: {weather['temperature']}°C")
        print(f"Descriere: {weather['description']}")
    else:
        print(weather["error"])
