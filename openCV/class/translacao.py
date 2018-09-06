import numpy as np 
import cv2

def posicao(i, j, desl):
	return i + desl[1], j + desl[0]

def translacao(fundo, imagem, deslocamento):
	rows, cols = imagem.shape
	for i in range(rows):
		for j in range(cols):
			x, y = posicao(i, j, deslocamento)
			if x < rows and y < cols:
				fundo[x][y] = imagem[i][j]
