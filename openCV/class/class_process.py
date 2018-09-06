import cv2
import numpy as np 
import matplotlib.pyplot as plt
from rotacao      import *
from translacao   import *
from interpolacao import *
from cisalhamento import cisalha

class ImageProcess:
	'''
		As imagens processadas irao estar
	Salvas em dicionario onde as chaves sao:
	img  = imagem de entrada
	tra  = imagem transladada
	rot  = imagem rotacionada
	fft  = FFT da imagem
	dft  = DFT da imagem
	cis  = imagem cisalhada  
	'''
	def __init__(self, img):
		'''
			Inicia colocando uma 
		imagem dentro da classe.
		'''
		self.__dict = {'img' : img}
		self.__rows, self.__cols = img.shape

	def __createImage(self, key):
		'''
			Cria uma imgem para trabalhar.
		'''
		self.__dict[key] = np.zeros([self.__rows, self.__cols], dtype = np.uint8)

	def translacao(self, deslocamento):
		'''
			Translada a imagem sugundo
		um deslocamento dado.
		'''
		self.__createImage('tra')
		translacao(self.__dict['tra'], self.__dict['img'], deslocamento)

	def rotacao(self, centro, angulo):
		'''
			Rotaciona a Imagem com
		um dado angulo em graus man-
		tendo o pixel central inva-
		riante.
		'''
		self.__createImage('rot')
		rotation(self.__dict['rot'], self.__dict['img'], centro, degree_to_rad(angulo))
		interpol(self.__dict['rot'])

	def FFT(self):
		'''
			Transformada rapida de fourier
		'''
		pass

	def DFT(self):
		'''
			Transformada discreta de fourier
		'''
		pass

	def cisalhamento(self, anguloX = 0, anguloY = 0):
		'''
			Cisalha a imagem segundo os angulos 
		dados como argumento.
		'''
		self.__createImage('cis')
		cisalha(self.__dict['cis'], self.__dict['img'], degree_to_rad(anguloX), degree_to_rad(anguloY))
		interpol(self.__dict['cis'])

	def show(self, key):
		'''
			Esse metodo ira mostar a 
		imagem ate que o botao 'q' de
		'quit' seja prescionado.
		'''
		if not key in self.__dict.keys():
			print('Imagem nao existe')
			return

		cv2.imshow(key, self.__dict[key])
		while True:
			if chr(cv2.waitKey(1) & 0xFF) == 'q':
				break
		cv2.destroyAllWindows()

	def salvar(self, key, path):
		'''
			Salva a imagem no diretorio 
		dado como argumento.
		'''
		cv2.imwrite(path, self.__dict[key])