import numpy as np 
from matplotlib import pyplot as plt
from math import e, pi 

def gera_coluna(x, W, N):
	return [W**(u*x) for u in range(N)]

def DFT(f_x):
	N = len(f_x)
	W = e**((-2*pi*1j)/N)
	func = np.asmatrix(f_x)
	matrix_W = []
	for x in range(N):
		matrix_W.append(gera_coluna(x, W, N))
	matrix_W = np.asmatrix(matrix_W)
	return (np.asarray(func*matrix_W))[0]

if __name__ == '__main__':
	x   = [i for i in range(1024)]
	f   = [1 if i < 50 else 0 for i in range(1024)]
	dft = np.abs(DFT(f))
	plt.plot(x, dft)
	plt.show()