from tkinter import *
from bc import *
from math import pi, cos, sin, tan, asin, acos, atan


class SisBraco:
	def __init__(self, root):
		self.root = root
		self.__canvas = Canvas(root, width = 1600, height = 900, bg = 'white',takefocus=1, highlightthickness=0)
		self.__canvas.pack()
		self.braco = Braco(1600, 900, self.__canvas.create_oval, self.__canvas.create_line)
		self.arq = open('angs.txt', 'r')
		self.update()
		self.root.mainloop()

	def update(self):
		ang = self.arq.readline().split()
		try:
			s1 = float(ang[0])
			s2 = float(ang[1])
		except:
			s1 = 90
			s2 = 0
		self.braco.atualiza(self.__canvas.create_oval, self.__canvas.create_line, self.__canvas.delete, -s1, s2)
		self.root.after(5, self.update)


if __name__ == '__main__':
	root = Tk()
	SisBraco(root)