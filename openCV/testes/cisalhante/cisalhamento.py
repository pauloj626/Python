import cv2
import numpy as np 
from math import e, pi
from numpy import tan
import sys
from interpolacao import interpol

def degree_to_rad(angulo):
	return pi*angulo/180

def new_pos(x, y, angulo1, angulo2):
	return int(x+y*tan(angulo1)), int(y+x*tan(angulo2))

def cisalha(fundo, img, angulo1 = 0, angulo2 = 0):
	rows, cols = img.shape
	for x in range(rows):
		for y in range(cols):
			u, v = new_pos(x, y, angulo1, angulo2)
			if -1 < u < rows and -1 < v < cols:
				fundo[u][v] = img[x][y]

if __name__ == '__main__':
	img = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)

	fundo = cv2.imread('black.jpg', cv2.IMREAD_GRAYSCALE)

	cisalha(fundo, img, degree_to_rad(20))

	cv2.imshow('fundo1', fundo)

	cv2.waitKey(0)

	interpol(fundo)

	cv2.imshow('fundo2', fundo)

	cv2.waitKey(0)

	cv2.destroyAllWindows()