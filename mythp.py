#!/usr/bin/python
import bme280
import time
import os
import sys
#while True:
temperature,pressure,humidity = bme280.readBME280All()
#	os.system('clear')
temp = "Temperature: " + str(format(temperature, '.2f'))
pres =  "Pressure: " + str(format(pressure, '.2f'))
humid = "% Humidity: " + str(format(humidity, '.2f'))

#print ""
#print""
#time.sleep(5)
while True:
	data = sys.stdin.readline().strip()
	if data == "":
		print 'HTTP/1.0 200 OK'
		print ''
		print '<html><head><meta http-equiv="refresh" content="10"></head><body><p>'+temp+'<br />'+pres+'<br />'+humid+'<br /></p></body></html>'
		sys.stdout.flush()
		break;
