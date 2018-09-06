arq1 = open('2_off.TXT'  , 'r')
arq2 = open('2_off_1.txt', 'w')


s = arq1.readline()

while bool(s):
	if s != '\n':
		arq2.write(s)
	s = arq1.readline()

arq2.close()
arq1.close()
