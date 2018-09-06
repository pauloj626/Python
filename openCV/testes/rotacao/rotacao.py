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
 
def intensidade(img, i, j):
	k = 0
	n_k = 0
	for n in range(i-1, i+1):
		for m in range(j-1, j+1):
			if img[n][m] > 0:
				k += int(img[n][m])
				n_k += 1
	try:
		return np.uint8(k/n_k)
	except:
		return 0
	

def interpol(img):
	rows, cols = img.shape
	for i in range(1, rows - 1):
		for j in range (1, cols - 1):
			if img[i][j] == 0:
				img[i][j] = intensidade(img, i, j)


if __name__ == '__main__':
	fundo = cv2.imread('graywoman.jpg', cv2.IMREAD_GRAYSCALE)

	tigre = cv2.imread('graywoman.jpg', cv2.IMREAD_GRAYSCALE)

	rows, cols = tigre.shape

	rotation(fundo, tigre, (rows/2, cols/2), degree_to_rad(45))

	cv2.imshow('rotation', fundo)

	cv2.waitKey(0)

	interpol(fundo)

	cv2.imwrite('graywoman_r.jpg', fundo)

	cv2.imshow('interpol_rotation', fundo)

	cv2.waitKey(0)