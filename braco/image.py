import cv2
import numpy as np 

from matplotlib import pyplot as plt 

img = cv2.imread("aero.png", cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

th, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

floodfill = thresh.copy()

h, w = thresh.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

cv2.floodFill(floodfill, mask, (0,0), 255)

floodfill_inv = cv2.bitwise_not(floodfill)

im_without_hole = thresh + floodfill_inv

im_without_hole_copy = im_without_hole.copy()

contours, hierarchy = cv2.findContours(im_without_hole_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

zeros_img = np.zeros([rows, cols])

for i in range(len(contours)):
	cv2.drawContours(zeros_img, contours, i, 255, 1)

plt.imshow(zeros_img, cmap = 'gray')
plt.show()