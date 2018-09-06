from tkinter import *

class senha:
	def __init__(self, root):
		#defini as frames
		self.frame = []
		for i in range(5):
			self.frame.append(Frame(root))
			self.frame[i].pack()
		#Label PASSWORDS
		Label(self.frame[0], text = 'PASSWORDS', fg = 'darkblue',
			font = ('Verdana', '14', 'bold'), height = 3).pack()

		#Defini uma fonte
		font1 = ('Verdana', '10', 'bold')

		#Outra Label
		Label(self.frame[1], text = 'NOME: ', 
			font = font1, width = 8).pack(side = LEFT)

		#Defini uma Entry
		self.nome = Entry(self.frame[1], width = 10,
			font = font1)
		self.nome.focus_force() # O foco inicia com essa entry
		self.nome.pack(side = LEFT)

		#Defini outra Label
		Label(self.frame[2], text = 'SENHA: ',
			font = font1, width = 8).pack(side = LEFT)

		#Defini outra Entry
		self.senha = Entry(self.frame[2], width = 10, show = '*', #show = '*', só irá mostrar *
			font = font1)
		self.senha.pack(side = LEFT)

		#Defini Butão
		self.confere = Button(self.frame[3], font = font1, text = 'Conferir',
			bg = 'blue', command = self.conferir)
		self.confere.pack()

		#Defini Label
		self.msg = Label(self.frame[3], font = font1,
			height = 3, text = 'AGUARDANDO...')
		self.msg.pack()

	def conferir(self):
		nome = self.nome.get()
		senha = self.senha.get()
		if nome == senha:
			self.msg['text'] = 'ACESSO PERMITIDO'
			self.msg['fg'] = 'darkgreen'
		else:
			self.msg['text'] = 'ACESSO NEGADO'
			self.msg['fg'] = 'red'
			self.nome.focus_force()


root = Tk()
senha(root)
root.mainloop()