import cv2
import numpy as np 
from sistemaPlanetario import sistemaPlanetario
from time import sleep

class EspacoPlanetario:
	def __init__(self, root):
		self.__canvas = Canvas(root, width = 1600, height = 760, bg = 'black')
		self.__canvas.pack()
		'''
		self.frame = Frame(root)
		self.frame.pack()

		self.b = Button(self.frame, text = 'atualiza',
			bg = 'white', command = self.__update)
		self.b.pack()
		'''
		self.__sisPlan = sistemaPlanetario()
		

	def update(self):
		self.__sisPlan.atualizaSistema(self.__canvas.create_oval, self.__canvas.delete)


if __name__ == '__main__':
	root = Tk()

	a = EspacoPlanetario(root)

	a.update()

	root.mainloop()