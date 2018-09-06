from convert import *
import numpy as np 

class Plane:
	def __init__(self):
		self.__CM    = (     0,    0, 0.0)
		self.__beak  = ( 66.67,    0, 0.0)
		self.__left  = (-33.33, -100, 0.0)
		self.__right = (-33.33,  100, 0.0)
		self.__med   = (-33.33,    0, 0.0)
		self.__top   = (-33.33,    0, -50)
		self.normal  = (     0,    0, 1.0)

	def upDate(self, angs):
		self.__CM    = rotat_axes(self.__CM   , angs)
		self.__beak  = rotat_axes(self.__beak , angs)
		self.__left  = rotat_axes(self.__left , angs)
		self.__right = rotat_axes(self.__right, angs)
		self.__top   = rotat_axes(self.__top  , angs)
		self.__med   = rotat_axes(self.__med  , angs)
		self.normal  = rotat_axes(self.normal , angs)

	def __drawPart(self, part, canvas_draw, rows, cols):
		if part == 1:
			canvas_draw(self.__xCM+rows/2, self.__yCM+cols/2,
						self.__xLF+rows/2, self.__yLF+cols/2,
						self.__xBK+rows/2, self.__yBK+cols/2,
						self.__xRT+rows/2, self.__yRT+cols/2,
						self.__xCM+rows/2, self.__yCM+cols/2, fill = 'darkblue'  , tag = 'plane', outline = 'red')
		elif part == 2:
			canvas_draw(self.__xCM+rows/2, self.__yCM+cols/2,
						self.__xLF+rows/2, self.__yLF+cols/2,
						self.__xRT+rows/2, self.__yRT+cols/2,
						self.__xCM+rows/2, self.__yCM+cols/2, fill = 'dodgerblue', tag = 'plane', outline = 'darkblue')
		elif part == 3:
			canvas_draw(self.__xCM+rows/2, self.__yCM+cols/2,
						self.__xMD+rows/2, self.__yMD+cols/2,
						self.__xTP+rows/2, self.__yTP+cols/2,
						self.__xCM+rows/2, self.__yCM+cols/2, fill = 'blue'      , tag = 'plane', outline = 'yellow')

	def draw(self, canvas_draw, canvas_delet, rows, cols):
		canvas_delet('plane')
		self.__xCM, self.__yCM = point_to_projection2d(self.__CM   )
		self.__xBK, self.__yBK = point_to_projection2d(self.__beak )
		self.__xLF, self.__yLF = point_to_projection2d(self.__left )
		self.__xRT, self.__yRT = point_to_projection2d(self.__right)
		self.__xMD, self.__yMD = point_to_projection2d(self.__med  )
		self.__xTP, self.__yTP = point_to_projection2d(self.__top  )
		
		ppCM = proportion2d(self.__CM   )
		ppBK = proportion2d(self.__beak )
		ppLF = proportion2d(self.__left )
		ppRT = proportion2d(self.__right)
		ppMD = proportion2d(self.__med  )
		ppTP = proportion2d(self.__top  )

		ppMX = max(ppBK, ppLF, ppRT, ppMD, ppTP)

		self.__octant = octant(self.normal)

		if self.__octant in [1, 4, 5, 8]:
			self.__drawPart(1, canvas_draw, rows, cols)
			self.__drawPart(2, canvas_draw, rows, cols)
			self.__drawPart(3, canvas_draw, rows, cols)

		else:
			self.__drawPart(3, canvas_draw, rows, cols)
			self.__drawPart(2, canvas_draw, rows, cols)
			self.__drawPart(1, canvas_draw, rows, cols)