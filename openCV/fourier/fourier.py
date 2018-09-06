from matplotlib import pyplot as plt 
import numpy as np 
import cv2
from math import e, pi
from time import time

def W(v, y, N):
	return e**((-2*pi*v*y*1j)/N)

def fft_xv_valor(img_x, v, N):
	if len(img_x) < 2:
		return img_x[0]
	F_par   = fft_xv_valor(img_x[ ::2], v, N/2)
	F_impar = fft_xv_valor(img_x[1::2], v, N/2)
	return (F_par + W(v, 1, N)*F_impar)

def fft_xv_matriz(img):
	M, N = img.shape
	Fxv = np.ndarray([M, N], dtype = complex)
	for x in range(M):
		a = time()
		for v in range(N):
			Fxv[x][v] = fft_xv_valor(img[x], v, N)
	return Fxv

def fft2(img):
	M, N = img.shape
	Fxv = fft_xv_matriz(img)
	F = np.ndarray([M, N], dtype = complex)
	for v in range(N):
		col = [Fxv[i][v] for i in range(M)]
		for u in range(M):
			F[u][v] = fft_xv_valor(col, u, M)
	return F


if __name__ == '__main__':
	img = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)
	fft_xv_matriz(img)