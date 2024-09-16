# PyWeatherApp

PyWeatherApp este o aplicație Python care permite utilizatorilor să obțină prognoza meteo pentru un oraș specificat, folosind API-ul OpenWeatherMap.

## Funcționalități
- Obține prognoza meteo pentru orice oraș din lume
- Afișează temperatura în grade Celsius
- Oferă descrierea vremii

## Cerințe
- Python 3.x
- requests library (instalată automat din `requirements.txt`)
- Cheie API de la [OpenWeatherMap](https://openweathermap.org/api)

## Utilizare

Pentru a rula aplicația:

1. Rulează scriptul `run.py`:
    ```bash
    python run.py
    ```

2. După ce rulezi aplicația, ți se va cere să introduci numele unui oraș urmat de codul țării.

    - **Format**: `oras,tara` 
    - Exemplu: 
      - Pentru București, România: `Bucharest,RO`
      - Pentru Londra, Marea Britanie: `London,GB`
      - Pentru Paris, Franța: `Paris,FR`

    **Important**: Codul țării trebuie să fie specificat în format ISO 3166-1 alpha-2 (de exemplu, pentru România folosește `RO`, pentru Franța folosește `FR`, etc.).

3. Aplicația va returna temperatura și o descriere a vremii pentru orașul selectat.

## Exemplu

Dacă vrei să obții prognoza pentru București, România, introdu:
```bash
Introduceți numele orașului (oraș, țară): Bucharest,RO
