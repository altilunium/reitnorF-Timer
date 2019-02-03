import datetime
import os
import sys
import time
import pyperclip

def showCurrentDuration(start):
	now = datetime.datetime.now()
	delta = now - start
	delta_second = delta.seconds
	delta_hours = delta_second // 3600
	delta_second = delta_second - (delta_hours * 3600)
	delta_minute = delta_second // 60
	delta_second = delta_second - (delta_minute * 60)
	delta_fix = str(delta_hours) + " hour " + str(delta_minute) + " minute " + str(delta_second) + " second"
	os.system('cls')
	print "reitnorF Timer"
	print "(Press ctrl+c to stop the timer)"
	print "Started: "+ start.strftime("%d %B %Y - %H:%M")
	print delta_fix
	time.sleep(1)

os.system('cls')
begin = datetime.datetime.now()

try:
	while True:
		showCurrentDuration(begin)
except KeyboardInterrupt:
	pass


end = datetime.datetime.now()
delta = end - begin
delta_second = delta.seconds
delta_hours = delta_second // 3600
delta_second = delta_second - (delta_hours * 3600)
delta_minute = delta_second // 60
delta_second = delta_second - (delta_minute * 60)
delta_fix = str(delta_hours) + " hour " + str(delta_minute) + " minute "


string_report = "[" + begin.strftime("%d %B %Y") + "] " + begin.strftime("%H:%M") + "-"+ end.strftime("%H:%M") + " (" + delta_fix + ")"
pyperclip.copy(string_report)
print string_report
print "Report copied to your clipboard"