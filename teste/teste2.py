from tkinter import *

class Janela:
	def __init__(self, inst):
		self.frame = Frame(inst)
		self.frame.pack()

		self.texto = Label(self.frame, text = 'Clique para ficar amarelo')
		self.texto['width'] = 26
		self.texto['height'] = 3
		self.texto.pack()

		self.botao = Button(self.frame, text = 'Clique')
		self.botao['bg'] = 'green'
		#<Button-1> é o botão esquerdo do mouse
		#<Button-3> é o botão direito do mouse
		#<Motion> evento Movimento
		#<Leave>
		#<ButtonRelease-X> X = 1, 2 ou 3
		self.botao.bind("<Button-1>", self.mudarCor) 
		self.botao.pack()

	def mudarCor(self, event):
		if self.botao['bg'] == 'green':
			self.botao['bg'] = 'yellow'
			self.texto['text'] = 'Clique para ficar verde'
		else:
			self.botao['bg'] = 'green'
			self.texto['text'] = 'Clique para ficar amarelo'

root = Tk()
Janela(root)
root.mainloop()