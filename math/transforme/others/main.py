from matplotlib import pyplot as plt 
import numpy as np 
import cv2
from walsh import *
from trasforme import *

def normalize(img):
	m, M = img.min(), img.max()
	print(m, M, '<--')
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			img[i][j] = np.uint8((img[i][j] - m)/(M - m))
			print(i, j)

img = cv2.imread('graywoman.jpg', cv2.IMREAD_GRAYSCALE)
imWalsh = np.asarray(transforme(img, hadamard, float))
normalize(imWalsh)
cv2.imshow('walsh', np.uint8(imWalsh))
cv2.waitKey(0)
cv2.destroyAllWindows()