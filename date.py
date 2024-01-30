import os
from datetime import date
import locale
from dotenv import load_dotenv

load_dotenv()

# Import environment variables
LANGUAGE = os.getenv("LANGUAGE")
DATE_FORMAT = os.getenv("DATE_FORMAT")

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


def getDate(DATE_FORMAT):
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
