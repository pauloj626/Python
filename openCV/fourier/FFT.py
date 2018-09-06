import numpy as np 
from matplotlib import pyplot as plt 
from math import e, pi

def fft_linha(N, W, f_x):
	if len(f_x) < 2:
		return f_x[0]
	F_par   = fft_linha(2*N, W, f_x[ ::2])
	F_impar = fft_linha(2*N, W, f_x[1::2])
	return (F_par + (W**N)*F_impar) 

def FFT(f_x):
	N = len(f_x)
	W = e**((-2*pi*1j)/N)
	fft = [0j for _ in range(N)]
	for u in range(N):
		fft[u] = fft_linha(1, W**u, f_x)
	return np.asarray(fft)

if __name__ == '__main__':
	x   = [i for i in range(1024)]
	f   = [1 if i < 50 else 0 for i in range(1024)]
	fft = np.abs(FFT(f))
	plt.plot(x, fft)
	plt.show()