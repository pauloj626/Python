import cv2
import numpy as np 
from math import pi, cos, sin, tan, asin, acos, atan, sqrt, floor, ceil

from matplotlib import pyplot as plt 

img = cv2.imread("aero.png", cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

th, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

thresh = cv2.bitwise_not(thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

zeros_img = []

arq = open('angs.txt', 'w')
arq_int = open('angs_int.txt', 'w')

s1_old, s2_old = 0, 0

def to_degree(ang):
	return ang*180.0/pi

def deflexoes(i, j):
	global s1_old, s2_old
	x = j+100
	y = rows/2 - i if rows/2 - i != 0 else 1
	r = sqrt(x*x + y*y)
	if(r1+r2 > r):
		s1 = 90 - to_degree(acos((r*r + r1*r1 - r2*r2)/(2*r*r1)) - np.arctan2(y, x))
		s2 = to_degree(pi - acos((r1*r1 + r2*r2 - r*r)/(2*r1*r2)))
		
		s1, s2 = round(s1), round(s2)

		if((s1 != s1_old) or (s2 != s2_old)):
			arq_int.write(str(s1) + ' ' + str(s2) + '\n')
			s1_old, s2_old = s1, s2

def proximo_bit(i, j, img):
	indice = [ (1, 0),  (1, 1),  (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1),\
			   (2, 0),  (2, 1),  (2, 2),  (1, 2),  (0, 2),  (-1, 2), (-2, 2), (-2, 1), \
			  (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1 -2), (2, -2), (2, -1)]
	try:
		for xy in indice:
			if img[i+xy[0]][j+xy[1]]:
				return i+xy[0], j+xy[1]
		return 0
	except:
		return 0

for _ in contours:
	zeros_img.append(np.zeros([rows, cols]))

for n in range(len(contours)):
	cv2.drawContours(zeros_img[n], contours, n, 255, 1)

	r1 = 500
	r2 = 1000

	i = 0
	j = 0
	while j < cols:
		while (zeros_img[n][i][j] < 1):
			i+=1
			if i == rows:
				break
		if i < rows:
			zeros_img[n][i][j] = 0
			deflexoes(i, j)
			break
		i = 0
		j += 1

	while True:
		try:
			i, j = proximo_bit(i, j, zeros_img[n])
			zeros_img[n][i][j] = 0
			deflexoes(i, j)
		except:
			break