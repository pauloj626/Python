from tkinter import *

class Kanvas:
	def __init__(self, root):
		self.cavas1 = Canvas(root, width = 100, height = 200,
			cursor = 'X_cursor', bd = 5, bg = 'dodgerblue')
		self.cavas1.pack(side = LEFT)

		self.cavas2 = Canvas(root, width = 100, height = 200,
			cursor = 'dot', bd = 5, bg = 'purple')
		self.cavas2.pack(side = LEFT)

root = Tk()

Kanvas(root)

root.mainloop()