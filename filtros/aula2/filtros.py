from filtrar import *
import cv2

filtros = [np.asarray([[1.0/9 for _ in range(3)] for _ in range(3)]),\
		   np.asarray([[1/16.0, 2/16.0, 1/16.0], [2/16.0, 4/16.0, 2/16.0], [1/16.0, 2/16.0, 1/16.0]]),\
		   np.asarray([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),\
		   np.asarray([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),\
		   np.asarray([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])]



img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

for i in range(5):
	cv2.imwrite('filtro'+str(i+1)+'.png', func_filtar(img, filtros[i]))
