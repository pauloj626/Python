import cv2
from time import sleep

while True:
	x = cv2.waitKey(1) & 0xFF
	print(chr(x))
	sleep(0.2)

	if x == ord('q'):
		break