# PyWeatherApp

PyWeatherApp is a Python application that allows users to get the weather forecast for a specified city using the OpenWeatherMap API.

## Features
- Get the weather forecast for any city in the world
- Displays temperature in Celsius
- Provides a weather description

## Requirements
- Python 3.x
- `requests` library (automatically installed via `requirements.txt`)
- API key from [OpenWeatherMap](https://openweathermap.org/api)

## Usage

To run the application:

1. Run the `run.py` script:
    ```bash
    python run.py
    ```

2. After running the app, you will be prompted to enter a city name followed by the country code.

    - **Format**: `city,country`
    - Example: 
      - For Bucharest, Romania: `Bucharest,RO`
      - For London, United Kingdom: `London,GB`
      - For Paris, France: `Paris,FR`

    **Important**: The country code must be specified in ISO 3166-1 alpha-2 format (e.g., for Romania use `RO`, for France use `FR`, etc.).

3. The app will return the temperature and a weather description for the selected city.

## Example

If you want to get the forecast for Bucharest, Romania, enter:
```bash
Enter city name (city, country): Bucharest,RO
