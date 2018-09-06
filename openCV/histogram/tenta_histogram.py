from matplotlib import pyplot as plt 
import numpy as np 
import cv2

def prob(img, y):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			y[img[i][j]] += 1

x = [i for i in range(256)]
y = [0 for _ in range(256)]

img = cv2.imread('wiki.jpg', cv2.IMREAD_GRAYSCALE)

prob(img, y)

plt.bar(x, y, width = 1, color = 'r')

plt.show()