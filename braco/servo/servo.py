import serial 
import time

def serial_open(i):
	time.sleep(0.4)
	print('/dev/ttyACM' + str(i))
	return serial.Serial('/dev/ttyACM' + str(i), 9600)

def serial_chose():
	i = 0
	while True:
		try:
			ser = serial_open(i)
			return ser, i
		except:
			i += 1

ser, i = serial_chose()

arq = open('angs_int.txt', 'r')

s = 'a'

while bool(s):
	s = arq.readline()
	print(s)
	try:
		ser.write(s)
	except:
		ser, i = serial_chose()
	time.sleep(0.4)

print('\n\nFim')