import cv2
import numpy as np 

def contra_harmonic(img, i, j, n, q):
	try:
		x = img[i-(n//2):i+(n//2)+1, j-(n//2):j+(n//2)+1].flatten()
		return np.uint8((sum(x**(1+q)))/(sum(x**q)))
	except:
		return 0

def filter_contra_harmonic(img, n, q):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			img[i][j] = contra_harmonic(img, i, j, n, q)

if __name__ == '__main__':
	img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
	filter_contra_harmonic(img, 7, 2)
	cv2.imshow('contra_harmonic', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()