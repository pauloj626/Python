import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	( 1, -1, -1),
	( 1,  1, -1),
	(-1,  1, -1),
	(-1, -1, -1),
	( 1, -1,  1),
	( 1,  1,  1),
	(-1, -1,  1),
	(-1,  1,  1),
	)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)

surfaces = (
	(0, 1, 2, 3),
	(3, 2, 7, 6),
	(6, 7, 5, 4),
	(4, 5, 1, 0),
	(1, 5, 7, 2),
	(4, 0, 3, 6)
	)

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

'''
def Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
'''

vers_plan1 = (
			(0, 0, -1),
			(1, 0, 1),
			(0, 0, 0),
			(0, 0, -1)
			)

vers_plan2 = (
			(0, 0, -1),
			(-1, 0, 1),
			(0, 0, 0),
			(0,0,-1)
			)

def Plane():
	glBegin(GL_QUADS)
	x = 0
	for vertices in vers_plan1:
		x += 1
		glColor3fv(colors[x])
		glVertex3fv(vertices)
	glEnd()

	glBegin(GL_QUADS)
	x = 0
	for vertices in vers_plan2:
		x += 1
		glColor3fv(colors[x])
		glVertex3fv(vertices)
	glEnd()

def Cube():
	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		for vertex in surface:
			x += 1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()

	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

class Sphere(object):
	slices = 40
	stacks = 40

	def __init__(self, radius, position, color):
		self.radius = radius
		self.position = position
		self.color = color
		self.quadratic = gluNewQuadric()

	def render(self):
		glPushMatrix()
		glTranslatef(*self.position)
		glMaterialfv(GL_FRONT, GL_DIFFUSE  , (0.0, 0.0, 1.0))
		glMaterialfv(GL_FRONT, GL_AMBIENT  , (0.0, 0.0, 0.0, 1.0))
		glMaterialfv(GL_FRONT, GL_DIFFUSE  , (0.1, 0.5, 0.8, 1.0))
		glMaterialfv(GL_FRONT, GL_SPECULAR , (1.0, 1.0, 1.0, 1.0))
		glMaterialfv(GL_FRONT, GL_SHININESS, 5.0)
		glMaterialfv(GL_FRONT, GL_EMISSION , (0.0, 0.0, 0.0, 1.0))
		gluSphere(self.quadratic, self.radius,
				  Sphere.slices, Sphere.stacks)
		glPopMatrix()

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -10)

	glRotatef(25, 2, 1, 0)

	s = Sphere(1, (0, 0, 0), (0, 0, 0, 1))

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

		#glRotatef(1, 3, 1, 0)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		Plane()
		#s.render()
		pygame.display.flip()
		pygame.time.wait(10)

if __name__ == '__main__':
	main()