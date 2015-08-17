#!/usr/bin/env python

#Initial set up codes.
from Tkinter import *
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

#Actual GUI box.
root = Tk()
root.title("Relay Control")
root.geometry("400x400")
app = Frame(root)
app.grid()


#Label.
label = Label(app, text = "Simple Relay Control by Donovan Goodwin")
label.grid()

#Button Callbacks.
def Button1():  #Relay 1 on
	if button1:
		GPIO.output(35, GPIO.LOW)
		
def Button2():  #Relay 2 on
	if button2:
		GPIO.output(37, GPIO.LOW)

def Button3():  #Relay 1 off
	if button3:
		GPIO.output(35, GPIO.HIGH)
		
def Button4():  #Relay 2 off
	if button4:
		GPIO.output(37, GPIO.HIGH)

def Button5():  #All Relays on
	if button5:
		GPIO.output(35, GPIO.LOW)
		GPIO.output(37, GPIO.LOW)

def Button6():  #All Relays off
	if button6:
		GPIO.output(35, GPIO.HIGH)
		GPIO.output(37, GPIO.HIGH)

def Button7(): #Exit
	if button7:
		GPIO.cleanup()
		exit()
		
def Button8(): #Info
	if button8:
		value = root = Tk()
	root.title("About")
	root.geometry("450x200")
	app = Frame(root)
	app.grid()
	label = Label(app, text = 'Simple Relay Controler by Donovan Goodwin')
	label.grid()
	label2 = Label(app, text = 'This program is licenced under the GNU Gerneral Public License')
	label2.grid()
	label3 = Label(app, text = '''This program uses pin 35 and 37 on the Raspberry Pi,
 edit the .py file to change this.''')
	label3.grid()
	label4 = Label(app, text = 'This program is for normaly HIGH relays. To change this edit the .py file.')
	label4.grid()

#Buttons.
button1 = Button(app,text='Relay 1 on', command=Button1)
button1.grid()

button2 = Button(app,text='Relay 2 on', command=Button2)
button2.grid()

button3 = Button(app,text='Relay 1 off', command=Button3)
button3.grid()

button4 = Button(app,text='Relay 2 off', command=Button4)
button4.grid()

button5 = Button(app,text='All Relays on', command=Button5)
button5.grid()

button6 = Button(app,text='All Relays off', command=Button6)
button6.grid()

button7 = Button(app,text='Exit', command=Button7)
button7.grid()

button8 = Button(app,text='Info', command=Button8)
button8.grid()




#Loop starter.
root.mainloop()


