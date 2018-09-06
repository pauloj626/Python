import numpy as np
import cv2

img = cv2.imread('image/tiger.jpg', cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

img2 = np.ndarray((rows, cols), dtype = np.uint8)

img3 = np.ndarray((rows, cols), dtype = np.uint8)

for i  in range(rows/2):
	for j in range(cols/2):
		k = (img[2*i][2*j]/4) + (img[2*i][2*j+1]/4) + (img[2*i+1][2*j]/4) + (img[2*i+1][2*j+1]/4)
		img2[2*i][2*j]     = k
		img2[2*i][2*j+1]   = k
		img2[2*i+1][2*j]   = k 
		img2[2*i+1][2*j+1] = k

for i  in range(256):
	for j in range(256):
		k = img[4*i][4*j]
		img2[4*i][4*j]     = k
		img2[4*i][4*j+1]   = k
		img2[4*i][4*j+2]   = k 
		img2[4*i][4*j+3]   = k
		img2[4*i+1][4*j]   = k
		img2[4*i+1][4*j+1] = k
		img2[4*i+1][4*j+2] = k 
		img2[4*i+1][4*j+3] = k
		img2[4*i+2][4*j]   = k
		img2[4*i+2][4*j+1] = k
		img2[4*i+2][4*j+2] = k 
		img2[4*i+2][4*j+3] = k
		img2[4*i+3][4*j]   = k
		img2[4*i+3][4*j+1] = k
		img2[4*i+3][4*j+2] = k 
		img2[4*i+3][4*j+3] = k

cv2.imshow('resol', img2)
cv2.imshow('orig', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

print('rows = %d\ncols = %d'%(rows, cols))