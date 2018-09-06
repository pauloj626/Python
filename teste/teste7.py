from tkinter import *

class Fatia:
	def __init__(self, root):
		self.canvas = Canvas(root, width = 200, height = 200)
		self.canvas.pack()

		self.frame = Frame(root)
		self.frame.pack()

		self.__altura = 200

		self.canvas.create_oval( (25, self.__altura - 25 ,
								175, self.__altura - 175),
								fill = 'deepskyblue', outline = 'darkblue')

		fonte = ('Comic Sans MS', '14', 'bold')

		Label(self.frame, text = 'Fatia: ',
			font = fonte, fg = 'blue').pack(side = LEFT)

		self.porcentagem = Entry(self.frame, fg = 'red',
								font = fonte, width = 5)
		self.porcentagem.focus_force()
		self.porcentagem.pack(side = LEFT)

		Label(self.frame, text = '%', 
			font = fonte, fg = 'blue').pack(side = LEFT)

		self.botao = Button(self.frame, text = 'Desenhar',
							command = self.cortar, font = fonte,
							fg = 'darkblue', bg = 'deepskyblue')

		self.botao.pack(side = LEFT)


	def cortar(self):
		arco = self.canvas.create_arc

		fatia = float(self.porcentagem.get())*3.599

		self.canvas.delete('arco')

		arco(25, self.__altura - 25 ,
			175, self.__altura - 175,
			fill = 'yellow', outline = 'red',
			extent = fatia, tag = 'arco')

		self.porcentagem.focus_force()


root = Tk()

Fatia(root)

root.mainloop()


