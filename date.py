import os
import pytz
import locale
from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv()

# Import environment variables
LANGUAGE = os.getenv("LANGUAGE")
DATE_FORMAT = os.getenv("DATE_FORMAT")
COUNTRY_CODE = os.environ.get("COUNTRY_CODE")

today = date.today()


def setLang(lang):
    switcher = {
        "en": "en_EN.utf8",
        "fr": "fr_FR.utf8",
        "nl": "nl_NL.utf8"
    }
    match switcher.get(lang, "Invalid language"):
        case "Invalid language":
            print("Invalid language")
        case _:
            locale.setlocale(locale.LC_TIME, switcher.get(lang))
            print('Set language to : ', switcher.get(lang, "Invalid language"))

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


def getTime():
    current_time = datetime.now(get_utc(COUNTRY_CODE)["timezone"])
    return current_time.strftime("%H:%M")


def getDate():
    setLang(LANGUAGE)
    switcher = {
        "1" : "%d %m %Y",
        "2" : "%m %f %Y",
        "3" : "%d %B %Y",
        "4" : "%B %d %Y",
    }

    match switcher.get(DATE_FORMAT, "Invalid date format"):
        case "Invalid date format":
            return "Invalid date format"
        case _:
            return today.strftime(switcher.get(DATE_FORMAT))
