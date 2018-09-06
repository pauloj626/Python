import pygame
from pygame.locals import *
from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

colors = (
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(0, 0, 0),
	(1, 1, 1),
	(0, 1, 1),
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(0, 0, 0),
	(1, 1, 1),
	(0, 1, 1)
	)

class sphere:
	def __init__(self, x, y, z, raio, color):
		self.x     = x
		self.y     = y
		self.z     = z
		self.raio  = raio
		self.color = color
		rsqr = raio/sqrt(3) 
		self.__points = ((x + raio, y, z),        # 0
						 (x - raio, y, z),        # 1
						 (x, y + raio, z),        # 2
						 (x, y - raio, z),        # 3
						 (x, y, z + raio),        # 4
						 (x, y, z - raio),        # 5
				  (x + rsqr, y + rsqr, z + rsqr), # 6
				  (x + rsqr, y + rsqr, z - rsqr), # 7
				  (x + rsqr, y - rsqr, z + rsqr), # 8
				  (x + rsqr, y - rsqr, z - rsqr), # 9
				  (x - rsqr, y + rsqr, z + rsqr), # 10
				  (x - rsqr, y + rsqr, z - rsqr), # 11
				  (x - rsqr, y - rsqr, z + rsqr), # 12
				  (x - rsqr, y - rsqr, z - rsqr)  # 13
						 )

		self.__surface = ((0, 6, 7),
						  (0, 6, 8),
						  (0, 9, 7),
						  (0, 9, 8),
						  (1, 13, 12),
						  (1, 13, 11),
						  (1, 10, 12),
						  (1, 10, 11),
						  (2, 6, 7),
						  (2, 10, 11),
						  (2, 6, 10),
						  (2, 7, 11),
						  (3, 9, 7),
						  (),
						  (),
						  (),
						  (),
						  ())

	def drawPoints(self):
		glColor3fv(self.color)
		glBegin(GL_POINTS)
		for point in self.__points:
			glVertex3fv(point)
		glEnd()

	def drawSurface(self):
		global colors
		glColor3fv(self.color)
		glBegin(GL_TRIANGLES)
		for point in self.__surface:
			x = 0
			if bool(point):
				for i in point:
					x += 1
					glColor3fv(colors[x])
					glVertex3fv(self.__points[i])
		glEnd()

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -10)
	glRotatef(25, 2, 1, 0)
	#glTranslatef(0.0, 0.0, -4)
	#glRotatef(-90, 1, 0, 0)
	#glRotatef(30, 0, 0, 1)

	esp = sphere(0, 0, 0, 1, (1, 1, 0))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glRotatef(5, 0, 1, 0)
				if event.key == pygame.K_RIGHT:
					glRotatef(-5, 0, 1, 0)
				if event.key == pygame.K_UP:
					glRotatef(5, 1, 0, 0)
				if event.key == pygame.K_DOWN:
					glRotatef(-5, 1, 0, 0)
				if event.key == pygame.K_a:
					glRotatef(5, 0, 0, 1)
				if event.key == pygame.K_s:
					glRotatef(-5, 0, 0, 1)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0, 0, 1)
				if event.button == 5:
					glTranslatef(0, 0, -1)
		
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		esp.drawPoints()
		esp.drawSurface()
		pygame.display.flip()
		pygame.time.wait(10)

if __name__ == '__main__':
	main()