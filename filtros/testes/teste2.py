import cv2
import numpy as np 

def show(img):
	cv2.imshow('teste', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def criarImagem(rows, cols):
	return np.zeros([rows, cols])

def nivel(img, flt):
	valor = 0.0
	n, m = flt.shape
	for i in range(n):
		for j in range(n):
			valor += img[i][j]*flt[i][j]
	return valor

def filtro(img, flt):
	rows, cols = img.shape
	n, m = flt.shape
	img_filtrada = criarImagem(rows, cols)
	for i in range(n/2, rows - (n/2)):
		for j in range(n/2, cols - (n/2)):
			img_filtrada[i][j] = nivel(img[i-(n/2):i+(n+2)/2, j-(n/2):j+(n+2)/2], flt)
	return np.uint8(img_filtrada)

if __name__ == '__main__':
	img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
	#flt = np.asarray([[1.0/36.0 for _ in range(6)] for _ in range(6)])
	flt = np.asarray([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
	imgFitrada = filtro(img, flt)
	show(imgFitrada)
