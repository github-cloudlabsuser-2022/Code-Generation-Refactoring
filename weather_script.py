import requests

import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    if not city.strip():
        return None
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error: {str(e)}")
        return None

def display_weather(data):
    if __name__ == "__main__":
        try:
            city = input("Enter city name: ").strip()
            if not city:
                print("City name cannot be empty")
            else:
                weather_data = get_weather(city)
                display_weather(weather_data)
        except KeyboardInterrupt:
            print("\nProgram terminated by user")
if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)
