import datetime
import os
import sys
import time
import pyperclip
import threading
import signal

global timeToStop
global delta_fix
global now
timeToStop = False

		

def sig_handler(sig, frame):
	global timeToStop
	print("Exiting..")
	timeToStop = True




def showCurrentDuration(start):
	global delta_fix
	global now
	now = datetime.datetime.now()
	delta = now - start
	delta_second = delta.seconds
	delta_hours = delta_second // 3600
	delta_second = delta_second - (delta_hours * 3600)
	delta_minute = delta_second // 60
	delta_second = delta_second - (delta_minute * 60)
	delta_fix = str(delta_hours) + " hour " + str(delta_minute) + " minute " + str(delta_second) + " second"
	os.system('cls')
	print("reitnorF Timer")
	print("(Press ctrl+c to stop the timer)")
	print("Started: "+ start.strftime("%d %B %Y - %H:%M"))
	print(delta_fix)
	time.sleep(1)

os.system('cls')
begin = datetime.datetime.now()


signal.signal(signal.SIGINT, sig_handler)

while not timeToStop:
	showCurrentDuration(begin)	




string_report = "[" + begin.strftime("%d %B %Y") + "] " + begin.strftime("%H:%M") + "-"+ now.strftime("%H:%M") + " (" + delta_fix + ")"
pyperclip.copy(string_report)
print(string_report)
print("Report copied to your clipboard")
