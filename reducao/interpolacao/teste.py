import numpy as np 
import cv2

def show(img):
	cv2.imshow('teste', np.uint8(img))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def criarImagem(rows, cols):
	return np.zeros([rows, cols], dtype = float)

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
	imgAmpl = criarImagem(n*rows, n*cols)
	for i in range(rows):
		for j in range(cols):
			imgAmpl[i*n][j*n] = img[i][j]
	interpol(imgAmpl, rows, cols, n)
	return imgAmpl

if __name__ == '__main__':
	img = ampliacao('-8vezes.png', 8)
	show(img)
	cv2.imwrite('+8vezes_interpol.png', img)