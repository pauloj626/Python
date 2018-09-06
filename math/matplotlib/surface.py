import numpy as np 
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt 
from math import *
'''
def h_abs(u, v):
	return sqrt(16 + 4*((cos(2*pi*u*0.01) + (cos(2*pi*v*0.01)))**2))
'''
def h_abs(u, v):
	return abs(-4 + 2*(cos(2*pi*(u-50)*0.01) + cos(2*pi*(v-50)*0.01)))

def set_x(X):
	for j in range(100):
		for i in range(100):
			X[i][j] = j

def set_y(Y):
	for i in range(100):
		for j in range(100):
			Y[i][j] = i

def set_z(Z):
	for i in range(100):
		for j in range(100):
			Z[i][j] = h_abs(X[i][j], Y[i][j])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.zeros([100, 100])
Y = np.zeros([100, 100])
Z = np.zeros([100, 100])

set_x(X)
set_y(Y)
set_z(Z)

ax.plot_wireframe(X, Y, Z)

plt.show()