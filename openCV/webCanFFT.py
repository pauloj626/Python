import cv2
import numpy as np 
import matplotlib.pyplot as plt

def imgFFT(img):
	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)
	return 20*np.log(np.abs(fshift))

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	img = imgFFT(gray)

	plt.imshow(img, cmap = 'gray')

	plt.show()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()