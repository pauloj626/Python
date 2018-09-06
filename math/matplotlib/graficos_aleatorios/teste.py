import numpy as np 
from math import *
from matplotlib import pyplot as plt 

def func1(x, arg):
	return 0.5*((x**arg[0])+(x**arg[1]))

def func2(x, E):
	if x <= 0.5:
		return (0.5/(cosh(E*0.5) - 1))*(e**(E*x) - 1)
	return (1/(1 - e**(-E*0.5)))*(1 - e*(-E*x))

def list_func(X, func, arg):
	return [func(x, arg) for x in X]

if __name__ == '__main__':
	X = [i/1000.0 for i in range(1001)]
	Y = list_func(X, func1, (15, 0.3))
	plt.plot(Y, X)
	plt.show()