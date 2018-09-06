from tkinter import *

class Janela:
	def __init__(self, instTK):
		self.fr1 = Frame(instTK)
		self.fr1.pack()
		self.botao = Button(self.fr1, text = 'Oi', background = 'green')
		self.botao.pack()

root = Tk()

Janela(root)

root.mainloop()