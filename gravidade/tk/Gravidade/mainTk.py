from tkinter import *
from sistemaPlanetario import sistemaPlanetario

class EspacoPlanetario:
        def __init__(self, root):
                self.root=root
                self.__canvas = Canvas(root, width = 1600, height = 760, bg = 'black',takefocus=1, highlightthickness=0)
                self.__canvas.pack()
                self.__sisPlan = sistemaPlanetario()
                self.update()
                self.root.mainloop()
                
        def update(self):
                self.__sisPlan.atualizaSistema(self.__canvas.create_oval, self.__canvas.delete)
                self.root.after(10, self.update)


if __name__ == '__main__':
	r = Tk()
	EspacoPlanetario(r)

	
