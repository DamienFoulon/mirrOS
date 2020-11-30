#!/usr/bin/python3.9
#Open Source Software made by Damien Foulon
#Everybody can use it but notify my name in your modified files
#Enjoy the share ! (We are stronger together.)

import date, clock, weather, tkinter
from tkinter import *

gui = tkinter.Tk()

################
### Settings ###
###    My    ###
###  Window  ###
################

gui.overrideredirect(True)
gui.geometry("{0}x{1}+0+0".format(gui.winfo_screenwidth(), gui.winfo_screenheight()))
gui.title("mirrOS")
gui.configure(bg='#000')

################
###   Date   ###
###  Module  ###
################
label_date = Label(gui, text=date.currentDate, font=("Mirror 82", 40), bg='#000', fg='white')
label_date.pack()

################
###  Clock   ###
###  Module  ###
################
#label_Hour = Label(gui, text=clock.h, font=("Mirror 82", 40), bg='#000', fg='white')
#label_Hour.pack()
#label_Minute = Label(gui, text=clock.m, font=("Mirror 82", 40), bg='#000', fg='white')
#label_Minute.pack()
#label_Second = Label(gui, text=clock.s, font=("Mirror 82", 20), bg='#000', fg='white')
#label_Second.pack()

gui.mainloop()


