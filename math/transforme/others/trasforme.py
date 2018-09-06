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

def transforme(img, form_f, type):
	rowls, cols = img.shape
	g1 = matrx(form_f, type, rowls, rowls)
	g2 = matrx(form_f, type, cols, cols)
	img_mx = np.asmatrix(img)
	return g1*img_mx*g2

if __name__ == '__main__':
	img = cv2.imread('graywoman_r.jpg', cv2.IMREAD_GRAYSCALE)
	sh = shift_img(img)
	dft = DFT(DFT(sh))
	dft_abs = np.abs(dft)
	dft_show = np.uint8(normalize(dft_abs))
	cv2.imshow('tentativa', dft_show)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
