import numpy as np 
import cv2

def posicao(i, j, desl):
	return i + desl[0], j + desl[1]

def tralacao(fundo, imagem, deslocamento):
	rows, cols = imagem.shape
	for i in range(rows):
		for j in range(cols):
			x, y = posicao(i, j, deslocamento)
			if x < rows and y < cols:
				fundo[x][y] = imagem[i][j]


img = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)

fundo = cv2.imread('black.jpg', cv2.IMREAD_GRAYSCALE)

tralacao(fundo, img, (100, 512))

cv2.imshow('tralacao', fundo)

cv2.waitKey(0)

cv2.destroyAllWindows()