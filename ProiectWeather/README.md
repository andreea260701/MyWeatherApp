# PyWeatherApp

PyWeatherApp este o aplicație simplă Python care permite utilizatorilor să obțină prognoza meteo folosind OpenWeatherMap API.

## Funcționalități
- Obține prognoza meteo pentru orice oraș din lume
- Afișează temperatura în grade Celsius
- Oferă descrierea vremii

## Cerințe
- Python 3.x
- requests library

## Instalare

1. Clonează acest repository:
    ```bash
    git clone https://github.com/username/PyWeatherApp.git
    cd PyWeatherApp
    ```

2. Instalează dependențele:
    ```bash
    pip install -r requirements.txt
    ```

3. Obține o cheie API de la [OpenWeatherMap](https://openweathermap.org/api) și adaug-o în `pyweatherapp/config.py`.

4. Rularea aplicației:
    ```bash
    python -m pyweatherapp.weather city_name
    ```

## Rulare Teste
Pentru a rula testele:
```bash
python -m unittest discover tests
