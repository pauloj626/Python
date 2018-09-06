from Tkinter import *
from tkMessageBox import *
from matplotlib import pyplot as plt 
import cv2

class ImageProcess:
	def __init__(self, root):
		self.__frame   = {}
		self.__imgs    = {}
		self.__widgeMS = {}
		self.__widgeMI = {}
		self.__widgeFT = {}
		self.__widgeRS = {}

		self.__frame['init'] = [Frame(root)]

		self.__frame['sec'] = [Frame(root), Frame(root), Frame(root)]

		self.__frame['flt'] = [Frame(root), Frame(root), Frame(root), Frame(root)]

		self.__frame['res'] = [Frame(root), Frame(root), Frame(root)]

		self.__pack('init')

		self.__widgeMenuInicial() 

	def __pack(self, key):
		for fr in self.__frame[key]:
			fr.pack()

	def __unpack(self, key):
		for fr in self.__frame[key]:
			fr.pack_forget()

	def __widgeMenuInicial(self):
		self.__widgeMI['lb']  = Label(self.__frame['init'][0], text = 'Digite a Imagem')
		self.__widgeMI['lb'].pack()

		self.__widgeMI['en']  = Entry(self.__frame['init'][0])
		self.__widgeMI['en'].pack()
		
		self.__widgeMI['bt']  = Button(self.__frame['init'][0], text = 'OK', command = self.__getImage)
		self.__widgeMI['bt'].pack()

	def __widgeMenuSecundario(self):
		self.__widgeMS['bt_flt'] = Button(self.__frame['sec'][0], text = 'filtro', command = self.__setFilter)
		self.__widgeMS['bt_flt'].pack(side = LEFT)

		self.__widgeMS['bt_res'] = Button(self.__frame['sec'][0], text = 'resol', command = self.__setResol)
		self.__widgeMS['bt_res'].pack(side = LEFT)

		self.__widgeMS['bt_show'] = Button(self.__frame['sec'][1], text = 'show', command = self.__show)
		self.__widgeMS['bt_show'].pack(side = LEFT)

		self.__widgeMS['en'] = Entry(self.__frame['sec'][1])
		self.__widgeMS['en'].pack(side = LEFT)

		self.__widgeMS['bt_back'] = Button(self.__frame['sec'][2], text = '<< back', command = lambda : self.__backMenu('sec', 'init'))
		self.__widgeMS['bt_back'].pack()

	def __widgeFilter(self):
		for i in range(3):
			for j in range(3):
				self.__widgeFT['en_'+str(i)+str(j)] = Entry(self.__frame['flt'][i], width = 10)
				self.__widgeFT['en_'+str(i)+str(j)].pack(side = LEFT)

		self.__widgeFT['bt_back'] = Button(self.__frame['flt'][3], text = '<< back', command = lambda : self.__backMenu('flt', 'sec'))
		self.__widgeFT['bt_back'].pack(side = LEFT)

		self.__widgeFT['lb'] = Label(self.__frame['flt'][3], text = 'key:')
		self.__widgeFT['lb'].pack(side = LEFT)

		self.__widgeFT['en_key'] = Entry(self.__frame['flt'][3], width = 10)
		self.__widgeFT['en_key'].pack(side = LEFT)

		self.__widgeFT['bt_ap'] = Button(self.__frame['flt'][3], text = 'apply', command = self.__applyFiter)
		self.__widgeFT['bt_ap'].pack(side = BOTTOM)

	def __widgeResol(self):
		self.__widgeRS['lb'] = Label(self.__frame['res'][0], text = 'Informe n:')
		self.__widgeRS['lb'].pack(side = LEFT)

		self.__widgeRS['en'] = Entry(self.__frame['res'][0], width = 10)
		self.__widgeRS['en'].pack(side = LEFT)

		self.__widgeRS['lb_key'] = Label(self.__frame['res'][1], text = 'key:')
		self.__widgeRS['lb_key'].pack(side = LEFT)

		self.__widgeRS['en_key'] = Entry(self.__frame['res'][1], width = 15)
		self.__widgeRS['en_key'].pack(side = LEFT)

		self.__widgeRS['bt_ap'] = Button(self.__frame['res'][2], text = 'apply', command = self.__applyResolucao)
		self.__widgeRS['bt_ap'].pack(side = RIGHT)

		self.__widgeRS['bt_back'] = Button(self.__frame['res'][2], text = '<< back', command = lambda : self.__backMenu('res', 'sec'))
		self.__widgeRS['bt_back'].pack(side = RIGHT)

	def __setFilter(self):
		if(not bool(self.__widgeFT)):
			self.__widgeFilter()
		self.__unpack('sec')
		self.__pack('flt')

	def __setResol(self):
		if(not bool(self.__widgeRS)):
			self.__widgeResol()
		self.__unpack('sec')
		self.__pack('res')

	def __show(self):
		pass

	def __applyFiter(self):
		pass

	def __applyResolucao(self):
		pass

	def __backMenu(self, key1, key2):
		self.__unpack(key1)
		self.__pack(key2)

	def __getImage(self):
		self.__imgs['img'] = cv2.imread(self.__widgeMI['en'].get(), cv2.IMREAD_GRAYSCALE)
		self.__widgeMI['en'].delete(0, 'end')
		if(self.__imgs['img'] == None):
			showerror('Erro', 'Image not found')
		else:
			self.__unpack('init')
			self.__pack('sec')
			if(not bool(self.__widgeMS)):
				self.__widgeMenuSecundario()


if __name__ == '__main__':
	root = Tk()
	ImageProcess(root)
	root.mainloop()