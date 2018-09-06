from planeta import Planeta

class sistemaPlanetario:
	constG = 1
	def __init__(self):
		self.__planetas = []
		self.__planetas.append(Planeta('a',  600, 500, 0,  -0.1, 170000, (0, 0, 255))    )
		self.__planetas.append(Planeta('b', 1040, 500, 0,    20,    550, (255, 0, 0))    )
		self.__planetas.append(Planeta('c', 1070, 500, 0,    23,      5, (190, 190, 190)))
		self.__planetas.append(Planeta('d',  400, 500, 0,   -30,    200, (0, 200, 100))  )
		self.__planetas.append(Planeta('d',  500, 500, 0,    40,    200, (255, 100, 100)))
		self.__numPla = len(self.__planetas)

	def __calculaAceleracao(self, i, j, pos):
		'''
		ax = GMx/r^3
		ay = GMy/r^3
		'''
		return sistemaPlanetario.constG*self.__planetas[j]['m']*(self.__planetas[j][pos] - self.__planetas[i][pos])/(((self.__planetas[i]['x'] - self.__planetas[j]['x'])**2 + (self.__planetas[i]['y'] - self.__planetas[j]['y'])**2)**(1.5))

	def __setAcel(self):
		for i in range(self.__numPla):
			ax = 0
			ay = 0
			for j in range(self.__numPla):
				if i != j:
					ax += self.__calculaAceleracao(i, j, 'x')
					ay += self.__calculaAceleracao(i, j, 'y')
			self.__planetas[i].setAceleracao(ax, ay)

	def __move(self):
		for p in self.__planetas:
			p.move()

	def atualizaSistema(self, canvas_draw):
		self.__setAcel()
		self.__move()
		for p in self.__planetas:
			p.draw(canvas_draw)
