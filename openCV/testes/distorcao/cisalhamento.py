import cv2
import numpy as np 
from math import e, pi
from numpy import sin, cos, tan
from interpolacao import interpol

def degree_to_rad(angulo):
	return pi*angulo/180

def new_pos(x, y, angulo1, angulo2):
	return int(x+y*tan(angulo1)), int(y+x*tan(angulo2))

def calcula_angulo(rows, cols, x, y, angulo1, angulo2):
	return degree_to_rad(angulo1*(cos(4*x/rows))), degree_to_rad(angulo2*(cos(y/cols)))

def cisalha(fundo, img, angulo1, angulo2):
	rows, cols = img.shape
	for x in range(rows):
		for y in range(cols):
			ang1, ang2 = calcula_angulo(rows, cols, x, y, angulo1, angulo2)
			print(ang1, ang2)
			u, v = new_pos(x, y, ang1, ang2)
			if -1 < u < rows and -1 < v < cols:
				fundo[u][v] = img[x][y]

if __name__ == '__main__':
	img = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)
	fundo = cv2.imread('black.jpg', cv2.IMREAD_GRAYSCALE)
	cisalha(fundo, img, 10, 0)
	cv2.imshow('fundo1', fundo)
	cv2.waitKey(0)
	interpol(fundo)
	cv2.imshow('fundo2', fundo)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

'''
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
'''