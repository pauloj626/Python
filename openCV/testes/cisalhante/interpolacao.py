import cv2
import numpy as np 

def intensidade(img, i, j):
	k = 0
	n_k = 0
	for n in range(i-1, i+1):
		for m in range(j-1, j+1):
			if img[n][m] > 0:
				k += int(img[n][m])
				n_k += 1
	try:
		return np.uint8(k/n_k)
	except:
		return 0

def interpol(img):
	rows, cols = img.shape
	for i in range(1, rows - 1):
		for j in range (1, cols - 1):
			if img[i][j] == 0:
				img[i][j] = intensidade(img, i, j)