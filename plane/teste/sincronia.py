import numpy as np

def setKals(arq):
	tempo = []
	ang = {'pitch':[], 'roll':[], 'yaw' : []}
	s = arq.readline()
	while bool(s):
		s = s.split()
		tempo.append(float(s[0]))
		ang['pitch'].append(float(s[1]))
		ang['roll'].append(float(s[2]))
		ang['yaw'].append(float(s[3]))
		s = arq.readline()
	arq.close()
	return tempo, ang

def setContr(arq):
	tempo = []
	cont = {'Aleron1' : [], 'Aleron2' : [], 'Leme1' : [], 'Leme2' : []}
	s = arq.readline()
	while bool(s):
		s = s.split()
		tempo.append(float(s[0]))
		cont['Aleron1'].append(float(s[1]))
		cont['Aleron2'].append(float(s[2]))
		cont['Leme1'].append(float(s[3]))
		cont['Leme2'].append(float(s[4]))
		s = arq.readline()
	arq.close()
	return tempo, cont


def getPoly(tempo, obj):
	z = 0.5*np.polyfit(tempo - tempo[0], obj, 66)
	return np.poly1d(z)

def getFinal(nome1, nome2):
	arq = (open(nome1, 'r'), open(nome2, 'r'))
	tempo1, ang  =  setKals(arq[0])
	tempo2, cont = setContr(arq[1])
	typeAngs = ('pitch'  , 'roll'   , 'yaw')
	typeCont = ('Aleron1', 'Aleron2', 'Leme1', 'Leme2')

	tempo1 = np.array(tempo1)
	tempo1 = tempo1 - tempo1[0]

	tempo2 = np.array(tempo2)
	tempo2 = tempo2 - tempo2[0]

	length = len(tempo1)

	finais = {'tempo' : np.array(tempo1)      ,
			  'pitch' : 0.5*np.array(ang['pitch']),
			  'roll'  : 0.5*np.array(ang['roll']) ,
			  'yaw'   : 0.5*np.array(ang['yaw'])  ,
			  'cont1' : np.zeros(length)      ,
			  'cont2' : np.zeros(length)      ,
			  'cont3' : np.zeros(length)      ,
			  'cont4' : np.zeros(length)       }

	for i in range(length):
		j = 0
		while tempo2[j] < tempo1[i]:
			j += 1		
		for n in range(1,4):
			finais['cont'+str(n)][i] = cont[typeCont[n]][j]

	return finais

if __name__ == '__main__':
	finais = getFinal('22_in.TXT', '2_off.txt')
	print(finais['cont2'])