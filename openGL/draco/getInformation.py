import numpy as np 
from math import *
from matplotlib import pyplot as plt 

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

def interval(a, b, T):
	i = j = 0
	while T[i] < a:
		i += 1
	while T[i + j] <= b:
		j += 1
	return i, j+i

if __name__ == '__main__':
	T  = []
	P  = []
	R  = []
	ax = []
	ay = []
	az = []
	set_variaveis(T, P, R, ax, ay, az, 1)
	#x, y = interval(2320, 3240, T)
	T = [t/1000.0 for t in T]
	
	dft = np.fft.fft(ax)
	lowpass = np.asarray([1 if not (200 < x < 300) else 0 for x in range(len(dft))])
	lowpass1 = np.asarray([1 if (200 < x < 300) else 0 for x in range(len(dft))])
	#lowpass = np.asarray([3/(2.0+2.0j) for x in range(len(dft))])
	new_az = np.fft.ifft(dft*lowpass)
	new_ax = np.fft.ifft(dft*lowpass1)
	#plt.plot(T, ax, label = 'ax')
	#plt.plot(T, ay, label = 'ay')
	#plt.plot(T, ax, label = 'az')
	#plt.plot(T,  R, label = 'roll')
	#plt.plot(T,  P, label = 'pitch')
	plt.plot(T, np.real(new_az), label = 'filter')
	plt.plot(T, np.real(new_ax), label = 'filter1')
	#plt.plot([i for i in range(len(dft))], np.abs(dft), label = 'dft')
	plt.legend()
	plt.show()
	'''
	z = []
	for i in range(150):
		lowpass = np.asarray([1 if i <= x < (i+1) else 0 for x in range(len(dft))])
		new_az = np.fft.ifft(dft*lowpass)
		z.append(max(np.abs(new_az)))
		#plt.plot(T, np.real(new_az), label = 'filter, %d'%i)
		#plt.legend()
		#plt.show()
	plt.plot([i for i in range(len(z))], z, label = 'amp')
	plt.legend()
	plt.show()
	'''
	