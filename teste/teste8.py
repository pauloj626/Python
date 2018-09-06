from tkinter import *
from time    import localtime

class Horas:
	def __init__(self, inst):

		self.canvas = Canvas(inst, width = 200, height = 100)
		self.canvas.pack()

		self.frame = Frame(inst)
		self.frame.pack()

		self.__altura = 100

		pol = self.canvas.create_polygon
		rec = self.canvas.create_rectangle
		self.texto = self.canvas.create_text
		self.fonte = ('BankGothic Md BT', '20', 'bold')

		pol(10 , self.__altura - 10,
			40 , self.__altura - 90,
			160, self.__altura - 90,
			190, self.__altura - 10, fill = 'darkblue')

		pol(18 , self.__altura - 15,
			45 , self.__altura - 85,
			155, self.__altura - 85,
			182, self.__altura - 15, fill = 'dodgerblue')

		rec(45, self.__altura - 35,
			90, self.__altura - 60, fill = 'darkblue', outline = '')

		rec(110, self.__altura - 35, 
			155, self.__altura - 60, fill = 'darkblue', outline = '')

		self.texto(100, self.__altura - 50, text = ':',
			font = self.fonte, fill = 'yellow')

		self.mostrar = Button(self.frame, text = 'Que horas são?',
			command  = self.mostra, font=('Comic Sans MS', '11', 'bold'), 
			fg='darkblue', bg='deepskyblue')

		self.mostrar.pack(side = LEFT)

	def mostra(self):
		self.canvas.delete('H')
		self.canvas.delete('M')

		HORA = str(localtime()[3])
		MINU = str(localtime()[4])

		self.texto(67.5, self.__altura-50, text=HORA, fill='yellow',
			font=self.fonte, tag='H')

		self.texto(132.5, self.__altura-50, text=MINU, fill='yellow',
			font=self.fonte, tag='M')

root = Tk()

Horas(root)

root.mainloop()