import matplotlib.pyplot as plt 
from math import e, pi
import os

sigma = 5.67*1e-8

T_inf = 273

def calc_variaveis(p, d):
	return (4*pi)*((d/2)**2), ((4/3)*pi*((d/2)**3))*p

def beta_alpha(tupla):
	A, m = calc_variaveis(tupla[0], tupla[3])
	global sigma
	global T_inf
	beta, alpha = (tupla[4]*A/m*tupla[1]), ((tupla[2]*sigma*A/(m*tupla[1])))

	def f(tempo, temperatura):
		return (beta*(T_inf - temperatura) + alpha*(temperatura**4) - alpha*(T_inf**4))
	
	return f


def k1(tempo, temperatura, f):
	return f(tempo, temperatura)

def k2(tempo, temperatura, k_1, passo, f):
	return f(tempo+passo/2, temperatura+(passo/2)*k_1)

def k3(tempo, temperatura, k_2, passo, f):
	return k2(tempo, temperatura, k_2, passo, f)

def k4(tempo, temperatura, k_3, passo, f):
	return f(tempo+passo, temperatura+passo*k_3)

def pegaParametros():
	p = float(input())
	c = float(input())
	e_grego = float(input())
	d = float(input())
	h = float(input())
	return p, c, e_grego, d, h

funcao = beta_alpha(pegaParametros())

temperatura = [float(input())]
tempo = [i*0.00000001 for i in range(100000)]
passo = 0.00000001

for i in range(99999):
	k_1 = k1(tempo[i], temperatura[i], funcao)
	k_2 = k2(tempo[i], temperatura[i], k_1, passo, funcao)
	k_3 = k3(tempo[i], temperatura[i], k_2, passo, funcao)
	k_4 = k4(tempo[i], temperatura[i], k_3, passo, funcao)
	temperatura.append(temperatura[i] + (passo/6)*(k_1+2*k_2+2*k_3+k_4))
'''
f, ax = plt.subplots(2, sharex = True)

ax[0].plot(tempo, temperatura)

ax[1].plot(tempo, [i for i in range(100000)])

plt.plot(tempo, temperatura)

plt.show()
'''

nome = 'plot1.txt'
indc_nome = 1

while(os.path.exists(nome)):
	indc_nome += 1
	nome = nome[:4] + str(indc_nome) + '.txt'

arq = open(nome, 'w')
arq.write(str(tempo).replace(', ', '\n').replace('[', '').replace(']', ''))
arq.write(str(temperatura).replace(', ', '\n').replace('[', '\n').replace(']', ''))
arq.close()