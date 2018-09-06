from tkinter import *
from plane import Plane
from surfaceControl import *
from sincronia import *
from random import randint as rint

finais = getFinal('22_in.TXT', '2_off.txt')
i = 1
ang = np.zeros(7)

class AirSpace:
	def __init__(self, root):
		self.__root   = root
		self.__canvas = Canvas(root, width = 760, height = 610, bg = 'black', takefocus=1, highlightthickness=0)
		self.__canvas.pack()
		self.__Plane  = Plane()
		self.__Aleron = [Aleron('left'), Aleron('right')]
		self.__Leme   = Leme('leme')
		self.update()
		self.__root.mainloop()
		
	def update(self):
		global finais
		global i
		global ang

		if i == len(finais['tempo']):
			i = 1

		thetas = (finais['pitch'][i] - finais['pitch'][i-1], 
				  finais['roll'][i] - finais['roll'][i-1], 
				  finais['yaw'][i] - finais['yaw'][i-1])

		conv = 1.0/10

		theta1 = conv*(finais['cont1'][i] - finais['cont1'][i-1])
		theta2 = conv*(finais['cont2'][i] - finais['cont2'][i-1])
		theta3 = conv*(finais['cont3'][i] - finais['cont3'][i-1])
		theta4 = conv*(finais['cont4'][i] - finais['cont4'][i-1])

		ang[3] += theta1
		ang[4] += theta2
		ang[5] += theta3
		ang[6] += theta4

		tempo  = finais['tempo'][i] - finais['tempo'][i-1]

		self.__Plane.upDate(thetas)
		self.__Plane.draw(self.__canvas.create_polygon, self.__canvas.delete, 760, 460)

		self.__Aleron[0].upDate(theta1)
		self.__Aleron[0].draw(self.__canvas.create_polygon, self.__canvas.delete,  300, 1000)
		self.__canvas.delete('text')
		self.__canvas.create_text(150, 580, text = '%.2f'%ang[3], font=('Arial','20','bold'), 
										anchor=CENTER, fill='white', tag = 'text')
		self.__Aleron[1].upDate(-1*theta1)
		self.__Aleron[1].draw(self.__canvas.create_polygon, self.__canvas.delete, 1220, 1000)
		self.__canvas.create_text(600, 580, text = '%.2f'%(-1*ang[3]), font=('Arial','20','bold'), 
										anchor=CENTER, fill='white', tag = 'text')
		self.__Leme.upDate(-1*theta3)
		self.__Leme.draw(self.__canvas.create_polygon, self.__canvas.delete, 760, 900)
		self.__canvas.create_text(375, 580, text = '%.2f'%(ang[4]), font=('Arial','20','bold'), 
										anchor=CENTER, fill='white', tag = 'text')
		
		self.__root.after(int(tempo), self.update)
		i += 1


if __name__ == '__main__':
	r = Tk()
	AirSpace(r)
