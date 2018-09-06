import numpy as np 
import cv2
from math import floor

def criarImagem(rows, cols, tipo):
	return np.zeros([rows + 1, cols + 1], dtype = tipo)

def fR(img, i, x, j, n):
	f11 = img[i][j]
	f12 = img[i+n][j]
	return (1.0*(i + n - x)*f12/(1.0*n)) + (1.0*(x - i)*f11/(1.0*n))

def value(img, x, y, n):
	i = (floor(x/n))*n
	j = (floor(y/n))*n
	return ((j + n - y)*fR(img, i, x, j, n)/n) + ((y - j)*fR(img, i, x, j + n, n)/n)

def interpol(img, rows, cols, n):
	for x in range(rows):
		for y in range(cols):
			img[x][y] = value(img, x, y, n)

def ampliacao(nome, n):
	img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
	rows, cols = img.shape
	imgAmpl = criarImagem(n*rows, n*cols, float)
	for i in range(rows):
		for j in range(cols):
			imgAmpl[i*n][j*n] = float(img[i][j])
	interpol(imgAmpl, n*rows, n*cols, n)
	return np.uint8(imgAmpl)

def reducao(nome, n):
	img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
	rows, cols = img.shape
	imgReduc = criarImagem(int(rows/n), int(cols/n), np.uint8)
	for i in range(int(rows/n)):
		for j in range(int(cols/n)):
			imgReduc[i][j] = img[int(i*n)][int(j*n)]
	return np.uint8(imgReduc)

def convert(N):
	if N > 0:
		return 1.0/N
	return -N

def resolucao(nome, N):
	if N < 0:
		n = convert(N)
		return reducao(nome, n)
	return ampliacao(nome, N)

if __name__ == '__main__':
	for i in range(1, 5):
		print('-'+str(2**i)+'vezes.png')
		img = resolucao('-'+str(2**i)+'vezes.png', 2**i)
		cv2.imwrite('+'+str(2**i)+'inter.png', img)