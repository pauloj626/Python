from planeta import Planeta

class sistemaPlanetario:
	constG = 1
	def __init__(self):
		self.__numPla = 3
		self.__planetas = []
		self.__planetas.append(Planeta('a', 450, 350, 20, -11, 200000))
		self.__planetas.append(Planeta('b', 950, 350, 0,  10, 200000))
		self.__planetas.append(Planeta('c', 600, 100, 0,   0, 100))

	def __calcAcal(self, i, j, pos):
		return sistemaPlanetario.constG*self.__planetas[j]['m']*(self.__planetas[j][pos] - self.__planetas[i][pos])/(((self.__planetas[i]['x'] - self.__planetas[j]['x'])**2 + (self.__planetas[i]['y'] - self.__planetas[j]['y'])**2)**(1.5))

	def __setAcel(self):
		for i in range(self.__numPla):
			ax = 0
			ay = 0
			for j in range(self.__numPla):
				if i != j:
					ax += self.__calcAcal(i, j, 'x')
					ay += self.__calcAcal(i, j, 'y')
			self.__planetas[i].setAceleracao(ax, ay)

	def __move(self):
		for p in self.__planetas:
			p.move()

	def atualizaSistema(self, canvas_draw, canvas_delet):
		self.__setAcel()
		self.__move()
		for p in self.__planetas:
			p.draw(canvas_draw, canvas_delet)
