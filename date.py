#!/usr/bin/python3.9
#Open Source Software made by Damien Foulon
#Everybody can use it but notify my name in your modified files
#Enjoy the share ! (We are stronger together.)

#####################
#### Date Module ####
#####################

# Required Modules
from datetime import date
import locale
today = date.today()

# Choose Display Mode
displayMode = "3"         # 1 = 'dd/mm/yyyy' 2 = 'mm/dd/yyyy' 3 = 'dd/Month/yyyy' 4 = 'Month/dd/yyyy'

# Choose Language
lang = "fr"               # view availables languages on https://github.com/DamienFoulon/mirrOS

# Setting Language
def setLang(lang):
    switcher = {
        "en" : "en_EN.utf8",
        "fr" : "fr_FR.utf8",
        "nl" : "nl_NL.utf8"
    }
    return switcher.get(lang, "nothing")
locale.setlocale(locale.LC_TIME, setLang(lang))

# Store current Date
def storeDate(displayMode):
    switcher = {
        "1" : "%d %m %Y",
        "2" : "%m %f %Y",
        "3" : "%d %B %Y",
        "4" : "%B %d %Y",
    }
    return switcher.get(displayMode, "nothing")

currentDate = today.strftime(storeDate(displayMode)) # Definitive date & disp mode

def showDate():
    print(currentDate)

showDate()