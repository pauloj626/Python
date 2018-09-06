import cv2
import numpy as np 

def binario(n):
	return 2**n

def set_bin(img, n):
	rows, cols = img.shape
	num_b = np.uint8(binario(n))
	for i in range(rows):
		for j in range(cols):
			img[i][j] = (img[i][j] & num_b)

img = cv2.imread('teste.jpg', cv2.IMREAD_GRAYSCALE)

set_bin(img, 7)

cv2.imshow('teste', img)

cv2.waitKey(0)

cv2.destroyAllWindows()