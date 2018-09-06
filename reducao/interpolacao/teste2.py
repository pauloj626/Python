import numpy as np 
import cv2

def criarImagem(rows, cols):
	return np.zeros([rows, cols], dtype = np.uint8)

def ampliacao(nome, n):
	img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
	rows, cols = img.shape
	imgAmpl = criarImagem(n*rows, n*cols)
	for i in range(rows):
		for j in range(cols):
			imgAmpl[i*n][j*n] = img[i][j]
	return imgAmpl

if __name__ == '__main__':
	imgAmpl = ampliacao('-8vezes.png', 8)
	cv2.imwrite('lenna2.png', imgAmpl)
	cv2.imshow('teste', imgAmpl)
	cv2.waitKey(0)
	cv2.destroyAllWindows()