#!/usr/bin/python3.9
#Open Source Software made by Damien Foulon
#Everybody can use it but notify my name in your modified files
#Enjoy the share ! (We are stronger together.)

# Required Modules
import datetime as dt
import time

def showClock():
    h = dt.datetime.now().hour
    m = dt.datetime.now().minute
    s = dt.datetime.now().second
    print(h)
    print(m)
    print(s)
    time.sleep(1)

showClock()