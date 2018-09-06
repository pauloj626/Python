import serial 
import time

ser = serial.Serial('/dev/ttyACM7', 9600)
srt = serial.Serial('/dev/ttyACM7', 9600)

arq = open('angs.txt', 'r')

s = 'a'

while bool(s):
	s = arq.readline()
	ser.write(s)
	srt.write(s)
	time.sleep(0.1)