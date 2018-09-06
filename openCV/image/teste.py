from Tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open('py.png')

photo = ImageTk.PhotoImage(image)

canvas = Canvas(root, width = 400, height = 400)

canvas.create_image(0, 0, image = photo)

canvas.pack()

root.mainloop()