from matplotlib import pyplot as plt 
import numpy as np 
import cv2

def hist(img, y):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			y[img[i][j]] += 1

def set_trasform(y, T):
	T[0] = y[0]
	for i in range(1, 256):
		T[i] = T[i-1] + y[i]
 
def equalizator(img, T):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			img[i][j] = np.uint8(((T[img[i][j]]*256)/cols)/rows)

x = [i for i in range(256)]

y = [0 for _ in range(256)]

img = cv2.imread('wiki.jpg', cv2.IMREAD_GRAYSCALE)

T = [0 for _ in range(256)]

hist(img, y)

set_trasform(y, T)

equalizator(img, T)

cv2.imshow('ten', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

'''
plt.plot(x, T)

plt.show()
'''