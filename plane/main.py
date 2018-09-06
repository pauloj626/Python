from tkinter import *
from plane import Plane
from surfaceControl import *
from random import randint as rint

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
                thetas = (rint(-3, 3), rint(-3, 3), rint(-3, 3))
                self.__Plane.upDate(thetas)
                self.__Plane.draw(self.__canvas.create_polygon, self.__canvas.delete, 760, 460)
                
                theta1 = rint(-10, 10)
                self.__Aleron[0].upDate(theta1)
                self.__Aleron[0].draw(self.__canvas.create_polygon, self.__canvas.delete,  300, 1000)
                self.__canvas.delete('text')
                self.__canvas.create_text(150, 580, text = '%.2f'%theta1, font=('Arial','20','bold'), 
                								anchor=CENTER, fill='white', tag = 'text')
                
                self.__Aleron[1].upDate(-1*theta1)
                self.__Aleron[1].draw(self.__canvas.create_polygon, self.__canvas.delete, 1220, 1000)
                self.__canvas.create_text(600, 580, text = '%.2f'%(-1*theta1), font=('Arial','20','bold'), 
                								anchor=CENTER, fill='white', tag = 'text')

                theta2 = rint(-10, 10)
                self.__Leme.upDate(theta2)
                self.__Leme.draw(self.__canvas.create_polygon, self.__canvas.delete, 760, 900)
                self.__canvas.create_text(375, 580, text = '%.2f'%(theta2), font=('Arial','20','bold'), 
                								anchor=CENTER, fill='white', tag = 'text')
                
                self.__root.after(50, self.update)


if __name__ == '__main__':
	r = Tk()
	AirSpace(r)
