import numpy as np 
import cv2

sin = np.sin
cos = np.cos
PI  = np.pi

def degree_to_rad(ang):
	return ang*PI/180

def posicao_rotacao(pos, centro, sin_ang, cos_ang):
	return int((pos[0] - centro[0])*cos_ang - (pos[1] - centro[1])*sin_ang), int((pos[0] - centro[0])*sin_ang + (pos[1] - centro[1])*cos_ang)

def rotation(fundo, img, centro, angulo):
	rows, cols = img.shape
	sin_ang, cos_ang = sin(angulo), cos(angulo)
	for i in range(rows):
		for j in range(cols):
			x, y = posicao_rotacao((i, j), centro, sin_ang, cos_ang)
			if (-1 < (x+centro[0]) < rows) and (-1 < (y+centro[1]) < cols):
				fundo[x+centro[0]][y+centro[1]] = img[i][j]