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
			( 0, 0+2, -1+t),
			( 0, 0+2,  0+t),
			( 0, 1+2,  0+t),
			( 0, 0+2, -1+t)
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

def axis():
	glBegin(GL_LINES)
	glColor3fv((1, 1, 0))
	glVertex3fv(( 0, 0.05, 0))
	glVertex3fv(( 1, 0.05, 0))
	glVertex3fv(( 0, 0.05, 0))
	glVertex3fv((-1, 0.05, 0))
	glColor3fv((0, 0, 1))
	glVertex3fv(( 0, 0.05, 0))
	glVertex3fv(( 0, 0.05, 1))
	glEnd()

def axisWhite():
	glBegin(GL_LINES)
	glColor3fv((1, 1, 1))
	glVertex3fv(( 0, 0.05, 0))
	glVertex3fv(( 0, 1.05, 0))
	glEnd()

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

	glMaterialfv(GL_FRONT, GL_AMBIENT  , (0.0, 0.0, 0.0, 1.0))
	glMaterialfv(GL_FRONT, GL_DIFFUSE  , (0.1, 0.5, 0.8, 1.0))
	glMaterialfv(GL_FRONT, GL_SPECULAR , (0.0, 0.0, 0.0, 1.0))
	glMaterialfv(GL_FRONT, GL_SHININESS, 10.0)
	glMaterialfv(GL_FRONT, GL_EMISSION , (0.0, 0.0, 0.0, 1.0))

	glTranslatef(0.0, 0.0, -10)

	glRotatef(0, 1, 0, 0)

	n = 0;

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glRotatef(5, 1, 0, 0)
				if event.key == pygame.K_RIGHT:
					glRotatef(5, 0, 1, 0)
				if event.key == pygame.K_UP:
					glRotatef(5, 0, 0, 1)
				if event.key == pygame.K_DOWN:
					glRotatef(-5, 1, 0, 0)
				if event.key == pygame.K_a:
					glRotatef(5, 0, 0, 1)
				if event.key == pygame.K_s:
					glRotatef(-5, 0, 0, 1)

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		#axisWhite()
		Plane()
		#axis()
		pygame.display.flip()
		try:
			pygame.time.wait(T[n+1] - T[n])
			glRotatef(5, 0, 0, 1) #Roll
			glRotatef(5, 1, 0, 0) #Pitch
			#glRotatef(P[n+1] - P[n], 1, 0, 0)
			#glRotatef(R[n+1] - R[n], 0, 0, 1)
			#n += 1
		except:
			pygame.quit()
			quit()

def set_variaveis(T, P, R, ax, ay, az, n):
	with open('%d.TXT'%n) as arq:
		try:
			while True:
				S = arq.readline().split()
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
	set_variaveis(T, R, P, ax, ay, az, 1)
	'''
	dft_R = np.fft.fft(R) 
	lowpass = np.asarray([1 if len(dft_R) - 30 <= x < len(dft_R) else 0 for x in range(len(dft_R))])
	new_R = np.fft.ifft(dft_R*lowpass)

	dft_P = np.fft.fft(P) # len(dft) = 863
	lowpass = np.asarray([1 if len(dft_R) - 30 <= x < len(dft_R) else 0 for x in range(len(dft_P))])
	new_P = np.fft.ifft(dft_P*lowpass)
	'''
	rodaAviao(T, P, R)