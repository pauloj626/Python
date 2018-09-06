from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image
import cv2

class TKImage:
	def __init__(self, root):
		self.__frame   = {}
		self.__widgeMI = {}

		self.__frame['init'] = [Frame(root), Frame(root)]

		self.__pack('init')

		self.__widgeMenuInicial()

	def __pack(self, key):
		for fr in self.__frame[key]:
			fr.pack() 

	def __widgeMenuInicial(self):
		#image = Image.fromarray(cv2.imread('lenna.png'))
		image = Image.open("lenna.png")
		photo = ImageTk.PhotoImage(image)

		self.__widgeMI['lb']  = Label(self.__frame['init'][0], image = photo)
		self.__widgeMI['lb'].image = photo
		self.__widgeMI['lb'].pack()
		
		self.__widgeMI['bt']  = Button(self.__frame['init'][1], text = 'OK', command = None)
		self.__widgeMI['bt'].pack()

if __name__ == '__main__':
	root = Tk()
	TKImage(root)
	root.mainloop()