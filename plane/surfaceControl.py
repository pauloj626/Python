from convert import *
import numpy as np 

class Aleron:
	def __init__(self, nome):
		self.__LF = ( 0, -100, 0)
		self.__LM = (50, -100, 0)
		self.__SM = (10, -100, 0)
		self.__DF = ( 0,  100, 0)
		self.__DM = (50,  100, 0)
		self.__FM = (10,  100, 0)
		self.nome = nome

	def upDate(self, theta):
		self.__LM = rotat_axes(self.__LM, (0, theta, 0))
		self.__DM = rotat_axes(self.__DM, (0, theta, 0))
		self.__SM = rotat_axes(self.__SM, (0, theta, 0))
		self.__FM = rotat_axes(self.__FM, (0, theta, 0))

	def draw(self, canvas_draw, canvas_delet, rows, cols):
		canvas_delet(self.nome)
		self.__xLF, self.__yLF = point_to_projection2d(self.__LF)
		self.__xLM, self.__yLM = point_to_projection2d(self.__LM)
		self.__xDF, self.__yDF = point_to_projection2d(self.__DF)
		self.__xDM, self.__yDM = point_to_projection2d(self.__DM)
		self.__xSM, self.__ySM = point_to_projection2d(self.__SM)
		self.__xFM, self.__yFM = point_to_projection2d(self.__FM)

		canvas_draw(self.__xLF+rows/2, self.__yLF+cols/2,
					self.__xLM+rows/2, self.__yLM+cols/2,
					self.__xDM+rows/2, self.__yDM+cols/2,
					self.__xDF+rows/2, self.__yDF+cols/2, 
					self.__xLF+rows/2, self.__yLF+cols/2, fill = 'blue'     , tag = self.nome, outline = 'red')

		canvas_draw(self.__xLF+rows/2, self.__yLF+cols/2,
					self.__xSM+rows/2, self.__ySM+cols/2,
					self.__xFM+rows/2, self.__yFM+cols/2,
					self.__xDF+rows/2, self.__yDF+cols/2, 
					self.__xLF+rows/2, self.__yLF+cols/2, fill = 'darkblue', tag = self.nome, outline = 'red')


class Leme:
	def __init__(self, nome):
		self.__TF = ( 0, 0, 60)
		self.__TM = (50, 0, 60)
		self.__SM = (15, 0, 60)
		self.__BF = ( 0, 0,-40)
		self.__BM = (50, 0,-40)
		self.__FM = (15, 0,-40)
		self.nome = nome

	def upDate(self, theta):
		self.__TM = rotat_axes(self.__TM, (0, 0, theta))
		self.__BM = rotat_axes(self.__BM, (0, 0, theta))
		self.__SM = rotat_axes(self.__SM, (0, 0, theta))
		self.__FM = rotat_axes(self.__FM, (0, 0, theta))

	def draw(self, canvas_draw, canvas_delet, rows, cols):
		canvas_delet(self.nome)
		self.__xTF, self.__yTF = point_to_projection2d(self.__TF)
		self.__xTM, self.__yTM = point_to_projection2d(self.__TM)
		self.__xBF, self.__yBF = point_to_projection2d(self.__BF)
		self.__xBM, self.__yBM = point_to_projection2d(self.__BM)
		self.__xSM, self.__ySM = point_to_projection2d(self.__SM)
		self.__xFM, self.__yFM = point_to_projection2d(self.__FM)

		canvas_draw(self.__xTF+rows/2, self.__yTF+cols/2,
					self.__xTM+rows/2, self.__yTM+cols/2,
					self.__xBM+rows/2, self.__yBM+cols/2,
					self.__xBF+rows/2, self.__yBF+cols/2, 
					self.__xTF+rows/2, self.__yTF+cols/2, fill = 'blue'     , tag = self.nome, outline = 'red')

		canvas_draw(self.__xTF+rows/2, self.__yTF+cols/2,
					self.__xSM+rows/2, self.__ySM+cols/2,
					self.__xFM+rows/2, self.__yFM+cols/2,
					self.__xBF+rows/2, self.__yBF+cols/2, 
					self.__xTF+rows/2, self.__yTF+cols/2, fill = 'darkblue', tag = self.nome, outline = 'red')