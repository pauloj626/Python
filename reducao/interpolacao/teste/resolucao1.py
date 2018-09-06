import numpy as np 
import cv2

def criarImagem(rows, cols, tipo):
	return np.zeros([rows, cols], dtype = tipo)

def linhas(img, rows, cols, n):
	for i in range(rows):
		for j in range(cols):
			for k in range(n):
				try:
					img[n*i][n*j+k] = img[n*i][n*j] + (img[n*i+n][n*j+n] - img[n*i][n*j])*((1.0*k)/n)
				except:
					img[n*i][n*j+k] = img[n*i][n*j] + (img[n*i+n-1][n*j+n-1] - img[n*i][n*j])*((1.0*k)/n)

def colunas(img, rows, cols, n):
	for i in range(rows):
		for j in range(n*cols):
			for k in range(n):
				try:
					img[n*i+k][j] = img[n*i][j] + (img[n*i+n][j] - img[n*i][j])*((1.0*k)/n)
				except:
					img[n*i+k][j] = img[n*i][j] + (img[n*i+n-1][j] - img[n*i][j])*((1.0*k)/n)

def interpol(img, rows, cols, n):
	linhas(img, rows, cols, n)
	colunas(img, rows, cols, n)

def ampliacao(nome, n):
	img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
	rows, cols = img.shape
	imgAmpl = criarImagem(n*rows, n*cols, float)
	for i in range(rows):
		for j in range(cols):
			imgAmpl[i*n][j*n] = img[i][j]
	interpol(imgAmpl, rows, cols, n)
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
	img = resolucao('-16vezes.png', 16)
	cv2.imshow('ampl.png', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

'''
	Caso queria reduzir a imagem use o n como negativo
ex:
img = resolucao('lenna.png', -16)
'''