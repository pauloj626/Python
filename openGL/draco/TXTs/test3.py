import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

import numpy as np

t = 1.0/3.0

vers_plan1 = (
			( 0, 0, -1+t),
			( 2, 0,  0+t),
			( 0, 0,  0+t),
			( 0, 0, -1+t)
			)

vers_plan2 = (
			( 0, 0, -1+t),
			(-2, 0,  0+t),
			( 0, 0,  0+t),
			( 0, 0, -1+t)
			)

vers_plan3 = (
			( 0, 0.15+2, -1+t),
			( 0, 0+2,  0+t),
			( 0, 0.3+2,  0+t),
			( 0, 0.15+2, -1+t)
			)

colors = (
	(0.2, 0.2, 0),
	(0, 0.2, 0.2),
	(0, 0.2, 0.2),
	(0, 0.2, 0),
	(0.3, 0.3, 0.3),
	(0.3, 0.3, 0.3),
	(0.2, 0.2, 0),
	(0, 0.2, 0),
	(0, 0, 0.2),
	(0, 0.2, 0),
	(0.1, 0.1, 0),
	(0, 0.1, 0.1)
	)

colors2 = (
	(0.9, 0.0, 0),
	(0.9, 0.2, 0),
	(0.9, 0.2, 0.1),
	(0.6, 0.2, 0),
	(0.6, 0.2, 0),
	(0.6, 0.1, 0.1),
	(0.6, 0.1, 0),
	(0.6, 0.0, 0)
	)

def Plane():
	glBegin(GL_QUADS)
	x = 0
	for vertices in vers_plan3:
		x += 1
		glColor3fv(colors2[x])
		glVertex3fv(vertices)
	glEnd()

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

def rodaAviao(T, P, R):
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(50, 1*(display[0]/display[1]), 0.1, 100.0)
	
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.3, 0.3, 0.3, 0.3])
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 2.0, 1.0, 1.0])
	glLightfv(GL_LIGHT0, GL_DIFFUSE, [ 0.0, 0.7, 0.7, 1.0])
	glEnable(GL_COLOR_MATERIAL)
	glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
	
	glTranslatef(0.0, 0.0, -10)

	glRotatef(20, 1, 0, 0)

	n = 0;

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Plane()
		pygame.display.flip()
		try:
			pygame.time.wait(T[n+1] - T[n])
			glRotatef(P[n+1] - P[n], 1, 1, 0)
			glRotatef(R[n+1] - R[n], 0, 0, 1)
			n += 1
		except:
			pygame.quit()
			quit()

def set_variaveis(T, P, R, ax, ay, az, n):
	with open('%d.TXT'%n) as arq:
		try:
			while True:
				S = arq.readline().replace(',', '').split()
				T.append(  int(S[0]))
				P.append(float(S[1]))
				R.append(float(S[2]))
				ax.append(float(S[3]))
				ay.append(float(S[4]))
				az.append(float(S[5]))
		except:
			arq.close()

if __name__ == '__main__':
	T  = []
	P  = []
	R  = []
	ax = []
	ay = []
	az = []
	set_variaveis(T, P, R, ax, ay, az, 11)
	rodaAviao(T, P, R)