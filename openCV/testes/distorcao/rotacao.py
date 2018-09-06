import numpy as np 
import cv2
from math import e as exp
from math import sqrt

sin = np.sin
cos = np.cos
PI  = np.pi

def degree_to_rad(ang):
	return ang*PI/180

def posicao_rotacao(pos, centro, sin_ang, cos_ang):
	try:
		return int((pos[0] - centro[0])*cos_ang - (pos[1] - centro[1])*sin_ang), int((pos[0] - centro[0])*sin_ang + (pos[1] - centro[1])*cos_ang)
	except:
		return -1, -1

'''
def calcula_angulo(i, j, centro, angulo):
	mx = max(centro)
	r = sqrt((i-mx)**2 + (j-mx)**2)
	return angulo*(exp**(-r/mx))
'''
def calcula_angulo(i, j, centro, angulo):
	mx = max(centro)
	r = sqrt((i-mx)**2 + (j-mx)**2)
	return angulo*cos(5*r/mx)

def rotation(fundo, img, centro, ang):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			angulo = degree_to_rad(calcula_angulo(i, j, centro, ang))
			print(angulo)
			sin_ang, cos_ang = sin(angulo), cos(angulo)
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
'''
if __name__ == '__main__':
	fundo = cv2.imread('black.jpg', cv2.IMREAD_GRAYSCALE)
	tiger = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)
	rows, cols = tiger.shape
	fourcc = cv2.cv.FOURCC('M', 'J', 'P', 'G')
	video  = VideoWriter('output.avi', frameSize = (cols, rows))
	video.open()
	print(video)
	for i in range(2):
		rotation(fundo, tiger, (rows/2, cols/2), i*20)
		interpol(fundo)
		video.write(fundo)
		print(video)
		fundo = cv2.imread('black.jpg', cv2.IMREAD_GRAYSCALE)

	video.release()
	print(video)
	


'''
if __name__ == '__main__':
	fundo = cv2.imread('black.jpg', cv2.IMREAD_GRAYSCALE)

	tigre = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)

	rows, cols = tigre.shape

	rotation(fundo, tigre, (rows/2, cols/2), 120)

	cv2.imshow('rotation', fundo)

	cv2.waitKey(0)

	interpol(fundo)

	cv2.imshow('interpol_rotation', fundo)

	cv2.waitKey(0)
