import matplotlib
import numpy as np
from math import *
import matplotlib.pyplot as plt

def read():
	x = []
	with open('g1000.txt') as arq:
		try:
			while True:
				x.append(float(arq.readline()))
		except:
			arq.close()
			return np.asarray(x)

def setX(dados):
	return np.asarray([i for i in range(int(min(dados)), int(max(dados))+1)])

def setY(dados, len_x):
	y = np.zeros(len_x)
	for dado in dados:
		y[int(dado - min(dados))] += 1
	return y

def media(dados):
	return sum(dados)/len(dados)

def desvio(dados):
	return np.sqrt(media(dados**2) - (media(dados))**2)

def gaussian_x(x, N, mi, sig):
	return (N/sqrt(2*pi*sig*sig))*(np.exp(-0.2*(((x-mi)/sig)**2)))

def gaussian(dados, x):
	N   = len(dados)
	mi  = media(dados)
	sig = desvio(dados)
	apr = np.zeros(len(x))
	for i in range(len(x)):
		apr[i] = gaussian_x(x[i], N, mi, sig)
	return apr


dados = read() 

x = setX(dados)

y = setY(dados, len(x))

plt.bar(x, y, width = 1)

x_new = [i/100.0 for i in range(min(x)*99, max(x)*101)]

gauss = gaussian(dados, x_new)

x_n = [n+0.5 for n in x_new]

plt.plot(x_n, gauss, color = 'red')

plt.show()
