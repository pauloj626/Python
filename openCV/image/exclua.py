import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

for i in range(rows):
	for j in range(cols):
		img[i][j] = (img[i][j])*((-1)**(i+j))

fft = np.fft.fft2(img)

fft = np.conj(fft)

img = np.real(np.fft.ifft2(fft))

for i in range(rows):
	for j in range(cols):
		img[i][j] = (img[i][j])*((-1)**(i+j))

plt.imshow(img, cmap = 'gray')
plt.title('Input image')
plt.show()
