from math import e

class Planeta:
	def __init__(self, nome, x, y, vx, vy, m, color):
		self.__pos = {'x': x , 'y':y, 'm':m}
		self.__vx = vx
		self.__vy = vy
		self.__ax = 0
		self.__ay = 0
		self.__r  = 20*(1-(e**(-(m**0.1)/5))) #formula apenas para caber no canvas
		self.__nome = nome
		self.__color = color

	def move(self):
		self.__vx += self.__ax
		self.__vy += self.__ay
		self.__pos['x']  += self.__vx
		self.__pos['y']  += self.__vy

	def draw(self, canvas_draw):
		canvas_draw((int(self.__pos['x']), int(self.__pos['y'])), int(self.__r), self.__color)

	def __getitem__(self, coord):
		return self.__pos[coord]

	def setAceleracao(self, ax, ay):
		self.__ax = ax
		self.__ay = ay