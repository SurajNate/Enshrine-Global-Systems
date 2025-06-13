# Call APIs here
# utils/api_helpers.py
import requests
import os

def fetch_spacex_next_launch():
    try:
        response = requests.get("https://api.spacexdata.com/v5/launches/next")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching SpaceX data:", e)
        return {}

def fetch_weather_by_coordinates(lat, lon):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("OpenWeather API key missing.")
        return {}

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching weather data:", e)
        return {}
