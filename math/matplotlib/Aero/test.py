import numpy as np 
import cv2
from matplotlib import pyplot as plt 
from math import pi

def createImage(rows, cols):
	return np.zeros([rows, cols])

def img_show(img, tle):
	plt.imshow(img, cmap = 'gray')
	plt.title(tle)
	plt.show()

def thresholding(img, value):
	rows, cols = img.shape
	imgBy = img > value
	imgThSh = createImage(rows, cols)
	for i in range(rows):
		for j in range(cols):
			if imgBy[i][j]:
				imgThSh[i][j] = 255
			else:
				imgThSh[i][j] = 0
	return imgThSh

if __name__ == '__main__':
	tipo = cv2.IMREAD_GRAYSCALE
	img  = cv2.imread('teste1.png', tipo)
	imgThSh = thresholding(img, 2) 
	img_show(imgThSh, 'cl')
	cv2.imwrite('pontos.png', imgThSh) 
	#img = (img/2)+100
	#cv2.imwrite('teste.png', img)