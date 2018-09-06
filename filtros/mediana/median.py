import cv2
import numpy as np 

def ordena(x, n):
	for i in range(n):
		for j in range(i-1, -1, -1):
			if(x[j] > x[j+1]):
				x[j], x[j+1] = x[j+1], x[j]
			else:
				break

def mediana(img, i, j, n):
	try:
		x = img[i-(n//2):i+(n//2)+1, j-(n//2):j+(n//2)+1].flatten()
		ordena(x, len(x))
		return x[(len(x)//2)]
	except:
		return 0

def filter_mediana(img, n):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			img[i][j] = mediana(img, i, j, n)

if __name__ == '__main__':
	img = cv2.imread('lenna_sp.png', cv2.IMREAD_GRAYSCALE)
	for _ in range(3):
		filter_mediana(img, 3)
	cv2.imshow('mediana', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()