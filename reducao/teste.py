import numpy as np 
import cv2

def criarImagem(rows, cols):
	return np.zeros([rows, cols], dtype = np.uint8)

def reducao(nome, n):
	img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
	rows, cols = img.shape
	imgReduc = criarImagem(int(rows/n), int(cols/n))
	for i in range(int(rows/n)):
		for j in range(int(cols/n)):
			imgReduc[i][j] = img[int(i*n)][int(j*n)]
	return imgReduc

if __name__ == '__main__':
	imgReduc = reducao('lenna.png', 0.1)
	cv2.imshow('teste', imgReduc)
	cv2.waitKey(0)
	cv2.destroyAllWindows()