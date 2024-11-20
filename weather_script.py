import requests
import os

API_KEY = '474d7f51606b1e7853b4b18161a22efb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'  # Fixed API version

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
    if data:
        print("\nWeather Information:")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("No weather data available")

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
