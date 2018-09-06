import numpy as np 
import cv2
from FFT import FFT
from matplotlib import pyplot as plt

def create_img(rows, cols):
	return np.ndarray([rows, cols], dtype = complex)

def imfft(img):
	rows, cols = img.shape
	img_ax = create_img(rows, cols)
	transf = create_img(rows, cols)
	for i in range(rows):
		img_ax[i] = FFT(img[i])
	for j in range(cols-1):
		ax = FFT(img_ax[0:rows, j:j+1].flatten())
		for i in range(rows):
			transf[i][j] = ax[i]
	return img_ax


if __name__ == '__main__':
	img = cv2.imread('graywoman.jpg', cv2.IMREAD_GRAYSCALE)
	img2 = imfft(img)
	plt.imshow(img2, cmap = 'gray')
	plt.show()
