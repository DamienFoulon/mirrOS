import math
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Import environment variables
OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
COUNTRY_CODE = os.environ.get("COUNTRY_CODE")
CITY_NAME = os.environ.get("CITY_NAME")
UNITS = os.environ.get("UNITS")

# Create a dictionary of settings
weathermap_settings = {"country_code": COUNTRY_CODE, "city_name": CITY_NAME, "units": UNITS}

if not OPEN_WEATHER_API_KEY or not COUNTRY_CODE or not CITY_NAME or not UNITS:
    raise Exception("Please set the environment variables in .env file")


def getWeather():
    # Build the URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{BASE_URL}appid={OPEN_WEATHER_API_KEY}&q={CITY_NAME},{COUNTRY_CODE}&units={UNITS}"

    try:
        # Fetch weather data from OpenWeatherMap API
        response = requests.get(complete_url)
        response.raise_for_status()  # Check for HTTP errors

        # Transform into python data from json object
        responseJSON = response.json()

        # Error handling
        match responseJSON["cod"]:
            case "401":
                print("Invalid API key")
            case "404":
                print("City not found or invalid Country Code")
            case 200:
                # Extracting data
                w = responseJSON["wind"]
                y = responseJSON["main"]
                z = responseJSON["weather"]
                return {
                    "city": responseJSON["name"],
                    "current_temperature": int(round(y["temp"], 1)),
                    "current_pressure": y["pressure"],
                    "current_humidity": y["humidity"],
                    "wind": {
                        "wind_speed": w["speed"],
                        "wind_degree": w["deg"],
                        "wind_direction": math.degrees(w["deg"]),
                    },
                    "weather_description": z[0]["description"],
                    "weather_state": z[0]["main"]
                }
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")

# Path: weather.py
