import cv2
import numpy as np 
from sistemaPlanetario import sistemaPlanetario
from time import sleep

class EspacoPlanetario:
	def __init__(self, img):
		self.__img = img
		self.__rows, self.__cols, _ = self.__img.shape
		self.__sisPlan = sistemaPlanetario()
		
	def __update(self):
		self.__sisPlan.atualizaSistema(lambda center, radius, color: cv2.circle(self.__img, center, radius, color, -1))

	def __canvasDelete(self):
		cv2.rectangle(self.__img, (0, 0), (self.__cols, self.__rows), (0, 0, 0), -1)

	def simulation(self, video):
		while True:
			self.__canvasDelete()
			self.__update()

			cv2.imshow('simulation', self.__img)

			video.write(self.__img)

			#sleep(0.02)

			self.__tecla = chr(cv2.waitKey(1) & 0xFF)
			if(self.__tecla == 'q'):
				break

		video.release()

		cv2.destroyAllWindows()


if __name__ == '__main__':
	img = cv2.imread('blackground.jpg', cv2.IMREAD_COLOR)
	rows, cols, _ = img.shape

	fourcc = cv2.cv.FOURCC(*'MJPG')
	video = cv2.VideoWriter('simulacao.avi', fourcc, 20, (cols, rows))

	spcPla = EspacoPlanetario(img)
	spcPla.simulation(video)