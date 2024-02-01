# Note : This feature is personal and not for public use unless if you leave in the city of Le Mans

import os
import requests
from dotenv import load_dotenv
from date import getDate, getTime
import time

load_dotenv()

# Import environment variables
LINE_ID = os.getenv("LINE_ID")
STOP_POINT_ID = os.getenv("STOP_POINT_ID")

if not LINE_ID or not STOP_POINT_ID:
    raise Exception("Please set the Setram's environment variables in .env file")


def getPublicTransportSchedule():
    # Build the URL
    BASE_URL = "https://pnp-ihm-lemans-prod.canaltp.fr/fr/full/schedule/next_time/"
    complete_url = f"{BASE_URL}?stop_area_id={STOP_POINT_ID}&line_id={LINE_ID}&date=Aujourd\'hui&time={getTime()}"

    directions = ["forward", "backward"]

    schedules = {}
    for i in directions:
        fetch_url = f"{complete_url}&direction_type={i}"
        try:
            # Fetch public transport data from Setram API
            response = requests.get(fetch_url)
            response.raise_for_status()  # Check for HTTP errors

            # Transform into python data from json object
            responseJSON = response.json()

            tramway_direction = list(responseJSON['schedule'].keys())[0]
            raw_schedules = responseJSON['schedule'][tramway_direction]

            temp_schedules = []

            for y in raw_schedules:
                timestamp = y.split('"')[1]
                # Check if the schedule is not already passed
                if timestamp > str(time.time()).split('.')[0]:
                    temp_schedules.append(timestamp)

            schedules[tramway_direction] = temp_schedules

        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")

    return schedules

def getNextTramway():
    schedule = getPublicTransportSchedule()
    forward = list(schedule.keys())[0]
    backward = list(schedule.keys())[1]

    return "Prochain tramway vers " + forward + " à " + time.strftime("%H:%M", time.localtime(int(schedule[forward][0]))) + " et vers " + backward + " à " + time.strftime("%H:%M", time.localtime(int(schedule[backward][0]))) + "."
