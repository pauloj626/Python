from matplotlib import pyplot as plt 
import numpy as np 
import cv2

def show(img):
	cv2.imshow('teste', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def creat_img(rows, cols):
	return np.zeros([rows, cols], dtype = float);

def nivel(img, filt):
	s = 0.0
	for u in range(3):
		for v in range(3):
			s += img[u][v]*filt[u][v]
	return s

def filter(img, filt):
	rows, cols = img.shape
	new_img = creat_img(rows, cols)
	for i in range(1, rows - 1):
		for j in range(1, cols - 1):
			new_img[i][j] = nivel(img[i-1:i+2, j-1:j+2], filt)
	return new_img

def normaliza(img):
	m, M = img.min(), img.max()
	print('m, M = ', m, M )
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			img[i][j] = np.uint8((255/(M-m))*(img[i][j] - m))


if __name__ == '__main__':
	img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
	#filt = np.asarray([[1/9.0, 1/9.0, 1/9.0], [1/9.0, 1/9.0, 1/9.0], [1/9.0, 1/9.0, 1/9.0]])
	filt = np.asarray([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
	print(filt)
	new_img = filter(img, filt)
	#normaliza(new_img)
	show(new_img)