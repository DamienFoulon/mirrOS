#!/usr/bin/python3.9
#Open Source Software made by Damien Foulon
#Everybody can use it but notify my name in your modified files
#Enjoy the share ! (We are stronger together.)

######################
### Weather Module ###
######################

# Required Modules
import requests, json

# Set your OWM API key
api_key = "529b3195936d28b1ed86f731f42ed826"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Country
country = ("fr")

# City
city_name = ("Le Mans")

# Units

units = ("metric")  #Standard, metric or imperial

# Creating complete URL

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&lang=" + country + "&units=" + units

# Return our response
response = requests.get(complete_url)

# Transform into python data
# from json object
x = response.json()

# Store data
# Only if the city was found
if x["cod"] != "404":
    #Store main key
    y = x["main"]

    currentTemp     = y["temp"]
    currentPressure = y["pressure"] 
    currentHumidity = y["humidity"]

    #Store weather key
    z = x ["weather"]

    weatherDescription = z[0]["description"]
    weatherState = z[0]["main"]

    #print("Température : " + 
    #                str(currentTemp) +
    #      "\n Préssion Athmosphérique : " +
    #                str(currentPressure) +
    #      "\n Humidité : " + 
    #                str(currentHumidity) + 
    #      "\n Description : " +
    #               str(weatherDescription))
else:
    print(" Ville non trouvée")

def setIcon(weatherState):
    switcher = {
        "Clear"         : "icons/clear.png",
        "Clouds"        : "icons/cloud.png",
        "Rain"          : "icons/rain.png",
        "Mist"          : "icons/mist.png",
        "Snow"          : "icons/snow.png",
        "Thunderstorm"  : "icons/storm.png",
    }
    return switcher.get(weatherState, "nothing")
#print(setIcon(weatherState))

def showWeather():
    print("Température : " + 
                    str(currentTemp) +
          "\n Préssion Athmosphérique : " +
                    str(currentPressure) +
          "\n Humidité : " + 
                    str(currentHumidity) + 
          "\n Description : " +
                   str(weatherDescription))
    print(setIcon(weatherState))