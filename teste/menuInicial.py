from Tkinter import *
import cv2

class menuInicial:
	def __init__(self, root):
		self.frame = Frame(root)
		self.frame.pack()

		self.label = Label(self.frame, text = 'Digite a Imagem')
		self.label.pack()

		self.entry = Entry(self.frame)
		self.entry.focus_force()
		self.entry.pack()

		self.button = Button(self.frame, text = 'OK', command = self.__getimage)
		self.button.pack()

		self.labelErro = None

	def __getimage(self):
		self.__urlImage = self.entry.get()
		self.__imagem = cv2.imread(self.__urlImage, cv2.IMREAD_GRAYSCALE)
		if(self.__imagem == None):
			self.__loadErro()

	def __loadErro(self):
		if(self.labelErro == None):
			self.labelErro = Label(self.frame, text = 'Image not found')
			self.labelErro.pack()

	def destroy(self):
		self.frame.destroy()
		return self.__imagem

if __name__ == '__main__':
	root = Tk()
	z = menuInicial(root)
	root.mainloop()