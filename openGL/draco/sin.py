import numpy as np 
from math import *
from matplotlib import pyplot as plt 

def set_variaveis(T, P, R, ax, ay, az, n):
	with open('%d.TXT'%n) as arq:
		try:
			while True:
				S = arq.readline().split()
				T.append(  int(S[0]))

				P.append(cos(0.01*T[len(T)-1]))

				R.append(cos(T[len(T)-1]))

				ax.append(cos(0.15*T[len(T)-1]))

				ay.append(float(S[4]))
				az.append(float(S[5]))
		except:
			arq.close()

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
	T  = []
	P  = []
	R  = []
	ax = []
	ay = []
	az = []
	set_variaveis(T, P, R, ax, ay, az, 5)
	
	z = T[0]

	T = [(x - z)/1000.0 for x in T]

	w = [i for i in range(len(T))]

	P = [e**(3.0j*t) for t in T]

	R = [cos(5*t) for t in T]

	dft = np.fft.fft(P) 
	plt.plot(w, np.abs(dft), label = 'P')
	
	dft = np.fft.fft(R) 
	plt.plot(w, np.abs(dft), label = 'R')
	'''
	dft = np.fft.fft(ax) 
	plt.plot(w, np.abs(dft), label = 'ax')
	'''
	plt.legend()
	plt.show()