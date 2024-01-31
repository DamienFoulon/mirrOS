import os
import pytz
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Import environment variables
COUNTRY_CODE = os.environ.get("COUNTRY_CODE")


# Get UTC from country code
def get_utc(country_code):
    try:
        # Load the timezone for the given country code
        country_timezone = pytz.country_timezones[country_code][0]

        # Get the timezone object
        timezone_object = pytz.timezone(country_timezone)

        # Get the current time
        current_time = datetime.now()

        # Get the UTC offset for the current time
        utc_offset = timezone_object.utcoffset(current_time).total_seconds() / 3600

        return {"utc": utc_offset, "timezone": timezone_object, "country_timezone": country_timezone}
    except KeyError:
        return None


def get_time(utc):
    current_time = datetime.now(get_utc(COUNTRY_CODE)["timezone"])
    return current_time


print(get_time(get_utc(COUNTRY_CODE)["utc"]).strftime("%H:%M"))
