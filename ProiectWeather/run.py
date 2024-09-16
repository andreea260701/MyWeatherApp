# run.py
from pyweatherapp.weather import display_weather

if __name__ == '__main__':
    city_name = input("Introduceți numele orașului: ")
    display_weather(city_name)
