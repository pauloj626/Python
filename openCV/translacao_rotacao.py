import numpy as np 
import cv2

image = cv2.imread('image/tiger.jpg')

altura, largura, _ = image.shape

#traslacao
deslocamento = np.float32([[1, 0, 25], [0, 1, 50]])

deslocado = cv2.warpAffine(image, deslocamento, (largura, altura))

cv2.imshow('traslacao', deslocado)

cv2.waitKey(0)

#Outro exemplo de translacao
deslocamento = np.float32([[1, 0, 50], [0, 1, -90]])

deslocado = cv2.warpAffine(image, deslocamento, (largura, altura))

cv2.imshow('traslacao', deslocado)

cv2.waitKey(0)

#Rotacao
centroRotacao = (largura/2, altura/2)

rotacao = cv2.getRotationMatrix2D(centroRotacao, 45, 1.0)

rotacionado = cv2.warpAffine(image, rotacao, (largura, altura))

cv2.imshow('rotacao', rotacionado)

cv2.waitKey(0)