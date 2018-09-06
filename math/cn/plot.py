import matplotlib.pyplot as plt 

def leia(nome, tempo, Temperatura):
	arq = open(nome, 'r')
	for i in range(100000):
		tempo.append(float(arq.readline()))
	for i in range(100000):
		Temperatura.append(float(arq.readline()))
	arq.close()

def prepara_plot(ax, tempo, Temperatura, title, i):
	a = 0 if (i in [0, 1]) else 1
	b = i%2
	ax[a, b].plot(tempo, Temperatura)
	ax[a, b].set_title(title)

def show_plot():
	tempo = []
	Temperatura = []
	title = ['0.8, 100', '0.0, 100', '0.8, 10', '0.0, 10']

	f, ax = plt.subplots(2, 2)

	for i in range(4):
		nome = 'plot'+ str(i+1)+'.txt'
		leia(nome, tempo, Temperatura)
		prepara_plot(ax, tempo, Temperatura, title[i], i)
		tempo = []
		Temperatura = []

	plt.show()