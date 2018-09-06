from tkinter import *
from bc import *
from math import pi, cos, sin, tan, asin, acos, atan, floor


class SisBraco:
	def __init__(self, root):
		self.root = root
		self.__canvas = Canvas(root, width = 1600, height = 1200, bg = 'white',takefocus=1, highlightthickness=0)
		self.__canvas.pack()
		self.braco = Braco(1600, 900, self.__canvas.create_oval, self.__canvas.create_line)
		self.arq = open('angs_blocks.txt', 'r')
		self.update()
		self.root.mainloop()

	def update(self):
		ang = self.arq.readline().split()
		try:
			self.s1 = float(ang[0])
			self.s2 = float(ang[1])
		except:
			pass
		self.braco.atualiza(self.__canvas.create_oval, self.__canvas.create_line, self.__canvas.delete, self.s1, self.s2)
		self.root.after(1, self.update)


if __name__ == '__main__':
	root = Tk()
	SisBraco(root)