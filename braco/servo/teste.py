'''
import serial 

ser = serial.Serial('/dev/ttyACM2', 9600)

a = ''

while a != 'q':
	a = raw_input("Ligar ou Desligar: ")
	ser.write(a)

import serial 
import time

ser = serial.Serial('/dev/ttyUSB1', 9600)

a = ''

while True:
	s = ser.readline()
	print(s)
	time.sleep(0.005)
'''

import serial 
import time

ser = serial.Serial('/dev/ttyACM2', 9600)

a = ''

while a != 'q':
	ser.write('l')
	time.sleep(0.1)
	ser.write('d')
	time.sleep(0.1)