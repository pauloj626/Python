import cv2
import numpy as np 
from math import pi, cos, sin, tan, asin, acos, atan, sqrt

from matplotlib import pyplot as plt 

img = cv2.imread("blocks.png", cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

th, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

thresh = cv2.bitwise_not(thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

zeros_img = np.zeros([rows, cols])

for i in range(len(contours)):
	cv2.drawContours(zeros_img, contours, i, 255, 1)

cv2.drawContours(zeros_img, contours, 1, 255, 1)

arq = open('angs.txt', 'w')

r1 = 1100
r2 = 1100

def to_degree(ang):
	return ang*180.0/pi

def deflexoes(i, j):
	x = j+100
	y = rows/2 - i if rows/2 - i != 0 else 1
	r = sqrt(x*x + y*y)
	if(r1+r2 > r):
		s1 = to_degree( -1*acos((r*r + r1*r1 - r2*r2)/(2*r*r1)) + np.arctan2(y, x))
		s2 = to_degree(pi - acos((r1*r1 + r2*r2 - r*r)/(2*r1*r2)))
		arq.write(str(s1) + ' ' + str(s2) + '\n')

i = 0
j = 0
while j < cols:
	while (zeros_img[i][j] < 1):
		i+=1
		if i == rows:
			break
	if i < rows:
		zeros_img[i][j] = 0
		deflexoes(i, j)
		break
	i = 0
	j += 1

def proximo_bit(i, j):
	indice = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
	try:
		for xy in indice:
			if zeros_img[i+xy[0]][j+xy[1]]:
				return i+xy[0], j+xy[1]
		return 0
	except:
		return 0

while True:
	try:
		i, j = proximo_bit(i, j)
		zeros_img[i][j] = 0
		deflexoes(i, j)
	except:
		break
