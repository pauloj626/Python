import numpy as np 
import cv2

def criarImagem(rows, cols):
	return np.zeros([rows, cols], dtype = np.uint8)

def convert(N):
	if N > 0:
		return 1.0/N
	return -N

def resolucao(nome, N):
	n = convert(N)
	img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
	rows, cols = img.shape
	imgReduc = criarImagem(int(rows/n), int(cols/n))
	for i in range(int(rows/n)):
		for j in range(int(cols/n)):
			imgReduc[i][j] = img[int(i*n)][int(j*n)]
	return imgReduc

def show(img):
	cv2.imshow('teste', imgReduc)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	imgReduc = resolucao('+16vezes.png', -16)
	cv2.imwrite('-16vezes.png', imgReduc)