from tkinter import *

class Linha:
	def __init__(self, root):
		self.canvas = Canvas(root, width = 400, height = 400,
			cursor = 'watch', bd = 5)
		self.canvas.pack()

		self.frame = Frame(root)
		self.frame.pack()

		self.last = [200, 200]

		self.func = [self.left, self.up, self.down, self.rigth]
		self.texts = ['ESQUERDA', 'CIMA', 'BAIXO', 'DIREITA']

		configs = {'fg':'darkblue', 'bg':'ghostwhite', 'relief':GROOVE, 
		'width':11,'font':('Verdana','8','bold')}

		self.buttons = []

		for i in range(4):
			self.buttons.append(Button(self.frame, configs, 
				text = self.texts[i], command = self.func[i]))
			self.buttons[i].pack(side = LEFT)



	def left(self):
		x, y = self.last[0] - 10, self.last[1]
		self.canvas.create_line(self.last, x, y, fill = 'red')
		self.last = [x, y]

	def rigth(self):
		x, y = self.last[0] + 10, self.last[1]
		self.canvas.create_line(self.last, x, y, fill = 'purple')
		self.last = [x, y]

	def up(self):
		x, y = self.last[0], self.last[1] - 10
		self.canvas.create_line(self.last, x, y, fill = 'yellow')
		self.last = [x, y]

	def down(self):
		x, y = self.last[0], self.last[1] + 10
		self.canvas.create_line(self.last, x, y, fill = 'blue')
		self.last = [x, y]


root = Tk()

Linha(root)

root.mainloop()