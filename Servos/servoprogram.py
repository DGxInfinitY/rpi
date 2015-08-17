#!/usr/bin/env python

#Initial set up codes.
from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,50)
p.start(7.5)


#Actual GUI box.
root = Tk()
root.title("Servo Door Unlocker")
root.geometry("400x400")
app = Frame(root)
app.grid()


#Label.
label = Label(app, text = "Simple Servo Door Unlocker by Donovan Goodwin")
label.grid()

#Button Callbacks.
def Button1():  #Unlock.
    if button1:
        value = p.ChangeDutyCycle(2.5)
        
def Button2():  #Lock.
	if button2:
		value = p.ChangeDutyCycle(12.5)
		
def Button3():  #Neutral.
	if button3:
		value = p.ChangeDutyCycle(7.5)
		
def Button4(): #Exit.
	if button4:
		p.cleanup
		time.sleep(.5)
		exit()


#Buttons.
button1 = Button(app,text='Unlock', command=Button1)
button1.grid()

button2 = Button(app,text='Lock', command=Button2)
button2.grid()

button3 = Button(app,text='Neutral', command=Button3)
button3.grid()


#Loop starter.
root.mainloop()

