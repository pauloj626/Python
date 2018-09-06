from matplotlib import pyplot as plt 
from math import e, pi
import numpy as np 
import cv2

def matrx(g_forme, type_mx, linhas, colunas):
	mx = np.ndarray([linhas, colunas], dtype = type_mx)
	for i in range(linhas):
		for j in range(colunas):
			mx[i][j] = g_forme(i, j, linhas)
	return np.asmatrix(mx)

def form_f(x, u, N):
	return e**(-1j*2*pi*x*u/N)

def DFT(img):
	rowls, cols = img.shape
	g1 = matrx(form_f, complex, rowls, rowls)
	g2 = matrx(form_f, complex, cols, cols)
	img_mx = np.asmatrix(img)
	return g1*img_mx*g2

def normalize(dft_abs):
	maxm = dft_abs.max()
	c = 255/np.log(1+maxm)
	return c*np.log(1+dft_abs)

def shift_img(img):
	rowls, cols = img.shape
	sh = np.ndarray([rowls, cols])
	for i in range(rowls):
		for j in range(cols):
			sh[i][j] = (img[i][j])*((-1)**(i+j))
	return sh

if __name__ == '__main__':
	img = cv2.imread('graywoman.jpg', cv2.IMREAD_GRAYSCALE)
	sh = shift_img(img)
	dft = DFT((sh))
	dft_abs = np.abs(dft)
	dft_show = np.uint8(normalize(dft_abs))
	cv2.imshow('tentativa', dft_show)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
