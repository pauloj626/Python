import numpy as np 
from math import *
from matplotlib import pyplot as plt 

def func1(x, E, m):
	beta = 1/E
	apha = (2*m*E - 1)/(2*E - 2*beta)
	if x <= apha:
		return beta*x
	elif x < 2*m - apha:
		return E*(x - apha) + beta*apha
	else:
		return beta*(x - (2*m - apha)) + (1 - beta*alpha) 

def list_func(X, func, E, m):
	return [func(x, E, m) for x in X]

if __name__ == '__main__':
	X = [i/1000.0 for i in range(1001)]
	Y = list_func(X, func1, 20, 1)
	plt.plot(X, Y)
	plt.show()