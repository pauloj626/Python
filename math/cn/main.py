from plot import *
import os

for i in range(4):
	nome = 'parametros'+str(i+1)+'.txt'
	os.system('python3 rungeKutta.py < '+nome)

show_plot()