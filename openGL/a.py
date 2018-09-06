import pygame
from pygame.locals import *
from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

vw = 0.01
tm = 0

def axis():
	glBegin(GL_LINES)
	glColor3fv((1, 0, 0))
	glVertex3fv((0, 0, 0))
	glVertex3fv((1, 0, 0))
	glColor3fv((0, 1, 0))
	glVertex3fv((0, 0, 0))
	glVertex3fv((0, 1, 0))
	glColor3fv((0, 0, 1))
	glVertex3fv((0, 0, 0))
	glVertex3fv((0, 0, 1))
	glEnd()

def plan():
	glBegin(GL_TRIANGLES)
	glColor3fv((0.3, 0, 0))
	glVertex3fv((0, 0, 1))
	glVertex3fv((0, 1, 1))
	glVertex3fv((1, 1, 1))
	glVertex3fv((0, 0, 1))
	glEnd()

def points(x, y, z):
	glPointSize(10)
	glBegin(GL_POINTS)
	glColor3fv((1, 1, 1))
	glVertex3fv((x, y, 1))
	glEnd()

def mudarPos():
	global vw
	global tm
	return cos(vw*tm), sin(vw*tm), sin(vw*tm)*cos(vw*tm)

def main():
	x = z = 1
	y = 0
	global tm
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -5)

	glRotatef(-90, 1, 0, 0)
	glRotatef(30, 0, 0, 1)

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
		axis()
		x, y, z = mudarPos()
		plan()
		points(x, y, z)
		pygame.display.flip()
		pygame.time.wait(10)
		tm += 10

if __name__ == '__main__':
	main()