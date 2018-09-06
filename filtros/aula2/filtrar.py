import cv2
import numpy as np 

def show(tupla_img):
	for text_img in tupla_img:
		cv2.imshow(text_img[0], text_img[1])
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
	return img_filtrada

def retirarNegativo(img):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			if(img[i][j] < 0):
				img[i][j] = 0
	return np.uint8(img)

def func_filtar(img, flt):
	return retirarNegativo(filtro(img, flt))

if __name__ == '__main__':
	img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
	flt = np.asarray([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
	imgFitrada = retirarNegativo(filtro(img, flt))
	show(('teste', imgFitrada))
	cv2.imwrite('lennaBorda.png', imgFitrada)

