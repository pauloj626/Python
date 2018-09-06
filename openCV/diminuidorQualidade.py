import cv2 
import numpy as np 

def media(img, n):
	k = 0
	for row in img:
		k += np.sum(row)

	return np.uint8(k/(n**2))

def igualaIntensidade(img, i, j, n, intesidade):
	for k in range(n):
		for m in range(n):
			img[n*i + k][n*j + m] = intesidade


def diminuiQualidade(img, n):
	a, b = img.shape
	for i in range(int(a/n)):
		for j in range(int(b/n)):
			intesidade = media(img[(n*i):(n*i+n), (n*j):((n*j)+n)], n)
			igualaIntensidade(img, i, j, n, intesidade)

img = cv2.imread('image/tiger.jpg', cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

print(rows, cols)

#fourcc = cv2.cv.FOURCC(*'MJGP')
#video = cv2.VideoWriter('video.avi', fourcc, 10, (cols, rows))

diminuiQualidade(img, 30)

cv2.imshow('img', img)

cv2.waitKey(0)

#video.release()

cv2.destroyAllWindows()