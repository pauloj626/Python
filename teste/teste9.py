from Tkinter import *
from tkMessageBox import *
from matplotlib import pyplot as plt 
import cv2

class ProcessImage:
	def __init__(self, root, img):
		self.__imgs = {}
		self.__imgs['img'] = img

		self.frame = Frame(root)
		self.frame.pack()

		self.buttonShow = Button(self.frame, text = 'Show', command = self.__show)
		self.buttonShow.pack(side = LEFT)

		self.label = Label(self.frame, text = 'Key')
		self.label.pack(side = LEFT)

		self.entry = Entry(self.frame)
		self.entry.pack()

	def __show(self):
		key = self.entry.get()
		try:
			plt.imshow(self.__imgs[key], cmap = 'gray')
			plt.show()
		except:
			showerror("Error", "Image Not Found")


if __name__ == '__main__':
	root = Tk()
	ProcessImage(root, cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE))
	root.mainloop()