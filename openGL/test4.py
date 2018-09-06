import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

points = (
		  (0, 0, 0),
		  (0, 0, 1),
		  (0, 1, 1),
		  (0, 1, 0),
		  (1, 1, 0),
		  (1, 0, 0),
		  (1, 0, 1),
		  (1, 1, 1),
		  )

G_OBJ_SPHERE = 2

def celula():
	glMatrixMode (GL_MODELVIEW);
	glLoadIdentity ();
	glRotatef (-20.0, 0.0, 0.0, 1.0);
	glBegin (GL_TRIANGLES);
	glVertex2f (0.0, 10.0);
	glVertex2f (-10.0, 0.0);
	glVertex2f (10.0, 0.0);
	glEnd ();

	qobj = gluNewQuadric()
	gluQuadricTexture(qobj, GL_TRUE)
	glBegin(GL_TRIANGLES)
	gluSphere(qobj, 1, 50, 50)
	gluDeleteQuadric(qobj)
	glEnd()

def make_sphere():
	glColor3fv((1, 1, 1))
	glNewList(G_OBJ_SPHERE, GL_COMPILE)
	quad = gluNewQuadric()
	gluSphere(quad, 0.5, 100, 100)
	gluDeleteQuadric(quad)
	glEndList()

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -10)

	glRotatef(0, 0, 0, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		#celula()
		make_sphere()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		pygame.display.flip()
		pygame.time.wait(10)

if __name__ == '__main__':
	main()