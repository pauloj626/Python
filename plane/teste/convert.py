import numpy as np
from math import pi

cov = 180.0/pi

def retang_to_polar(x, y):
	global cov
	r = np.sqrt(x**2 + y**2)
	return r, cov*np.arctan2(y, x)

def polar_to_retang(r, theta):
	global cov
	return r*np.cos(theta/cov), r*np.sin(theta/cov)

def rotat_1axe(P, eixo, ang):
	if eixo == 0:
		r, o = retang_to_polar(P[1], P[2])
		x, y = polar_to_retang(r, o + ang)
		return P[0], x, y
	if eixo == 1:
		r, o = retang_to_polar(P[0], P[2])
		x, y = polar_to_retang(r, o + ang)
		return x, P[1], y
	r, o = retang_to_polar(P[0], P[1])
	x, y = polar_to_retang(r, o + ang)
	return x, y, P[2]

def rotat_axes(P, angs):
	for i in range(3):
		P = rotat_1axe(P, i, angs[i])
	return P

def point_to_projection2d(P):
	r = np.sqrt(P[0]**2 + P[1]**2 + P[2]**2)
	if r == 0:
		return 0, 0
	d = P[0]/r
	_, o = retang_to_polar(P[1], P[2])
	return polar_to_retang(r*np.sqrt(1 - d**2), o)

def proportion2d(P):
	'''
	Observador em (2, 0, 0)
	'''
	r = np.sqrt((P[0]-1000)**2 + P[1]**2 + P[2]**2)
	return 1 - r/1000.0

def quadrant(x, y):
	_, o = retang_to_polar(x, y)
	if 0 <= o <= 90:
		return 1
	if 90 < o <= 180:
		return 2
	if -180 <= o <= -90:
		return 3
	return 4

def octant(P):
	x = quadrant(P[0], P[1])
	return x + (4 if P[2] < 0 else 0)
