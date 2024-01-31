# Note : This feature is personal and not for public use unless if you leave in the city of Le Mans

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Import environment variables
LINE_ID = os.getenv("LINE_ID")
STOP_POINT_ID = os.getenv("STOP_POINT_ID")

if not LINE_ID or not STOP_POINT_ID:
    raise Exception("Please set the Setram's environment variables in .env file")

def getPublicTransport():
    # Build the URL
    BASE_URL = "https://data.reseau-tan.fr/horairesarret.json?"
    complete_url = f"{BASE_URL}lineId={LINE_ID}&stopPointId={STOP_POINT_ID}"

    try:
        # Fetch public transport data from Setram API
        response = requests.get(complete_url)
        response.raise_for_status()  # Check for HTTP errors

        # Transform into python data from json object
        responseJSON = response.json()

        # Error handling
        match responseJSON["code"]:
            case 401:
                print("Invalid API key")
            case 404:
                print("City not found or invalid Country Code")
            case 200:
                # Extracting data
                return {
                    "line": responseJSON["line"],
                    "stop": responseJSON["stop"],
                    "next_passage": responseJSON["nextPassage"]
                }
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")