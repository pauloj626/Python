from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image

font = ('Verdana', '20', 'bold')

class TKImage:
	def __init__(self, root):
		self.__frame   = {}
		self.__widgeMI = {}
		self.__widgeMS = {}

		self.__frame['init'] = [Frame(root), Frame(root)]
		self.__frame['sec']  = [Frame(root), Frame(root), Frame(root), Frame(root), Frame(root)]

		self.__pack('init')

		self.__widgeMenuInicial()

	def __pack(self, key):
		for fr in self.__frame[key]:
			fr.pack() 

	def __unpack(self, key):
		for fr in self.__frame[key]:
			fr.pack_forget()

	def __widgeMenuInicial(self):
		image = Image.open("eletro.jpg")
		photo = ImageTk.PhotoImage(image)

		self.__widgeMI['lb']  = Label(self.__frame['init'][0], image = photo, font = font)
		self.__widgeMI['lb'].image = photo
		self.__widgeMI['lb'].pack()
		
		self.__widgeMI['bt']  = Button(self.__frame['init'][1], text = 'start', font = font, command = lambda : self.__setWidgeSec())
		self.__widgeMI['bt'].pack()

	def __widgeSec(self):
		self.__widgeMS['lb'] = Label(self.__frame['sec'][0], text = 'put the value of: ', font = font)
		self.__widgeMS['lb'].pack()

		self.__widgeMS['lb_V']  = Label(self.__frame['sec'][1], text = 'V = ', font = font)
		self.__widgeMS['lb_V'].pack(side = LEFT)

		self.__widgeMS['en_V']  = Entry(self.__frame['sec'][1], font = font)
		self.__widgeMS['en_V'].pack(side = LEFT)

		self.__widgeMS['lb_uV'] = Label(self.__frame['sec'][1], text = 'V', font = font)
		self.__widgeMS['lb_uV'].pack(side = LEFT)

		self.__widgeMS['lb_I']  = Label(self.__frame['sec'][2], text = 'I = ', font = font)
		self.__widgeMS['lb_I'].pack(side = LEFT)

		self.__widgeMS['en_I']  = Entry(self.__frame['sec'][2], font = font)
		self.__widgeMS['en_I'].pack(side = LEFT)

		self.__widgeMS['lb_uI'] = Label(self.__frame['sec'][2], text = 'mA', font = font)
		self.__widgeMS['lb_uI'].pack(side = LEFT)

		self.__widgeMS['lb_r']  = Label(self.__frame['sec'][3], text = 'r = ', font = font)
		self.__widgeMS['lb_r'].pack(side = LEFT)

		self.__widgeMS['en_r']  = Entry(self.__frame['sec'][3], font = font)
		self.__widgeMS['en_r'].pack(side = LEFT)

		self.__widgeMS['lb_ur'] = Label(self.__frame['sec'][3], text = 'cm', font = font)
		self.__widgeMS['lb_ur'].pack(side = LEFT)

		self.__widgeMS['bt_a']  = Button(self.__frame['sec'][4], text = 'apply', font = font, command = self.__applyValue)
		self.__widgeMS['bt_a'].pack()

	def __applyValue(self):
		V = float(self.__widgeMS['en_V'].get())
		I = float(self.__widgeMS['en_I'].get())
		r = float(self.__widgeMS['en_r'].get())
		ShowResult(Tk(), 4)

	def __setWidgeSec(self):
		self.__widgeSec()
		self.__gotoMenu('init', 'sec')

	def __gotoMenu(self, key1, key2):
		self.__unpack(key1)
		self.__pack(key2)

class ShowResult:
	def __init__(self, root, value):
		Label(root, text = "The valeu is:", font = font).pack()
		Label(root, text = str(value)+"C/kg", font = font).pack()
		Button(root, text = "Quit", font = font, command = root.destroy).pack()

if __name__ == '__main__':
	root = Tk()
	TKImage(root)
	root.mainloop()