import numpy as np 

def b(z, i):
	num = np.uint8(0x01)
	return 0 if z & (num << i) == 0 else 1

def walsh(x, u, N):
	value = float(1)
	for i in range(8):
		value = value * (1 if (b(x, i) * b(u, 7 - i)) == 0 else -1)
	print(value)
	return value

def hadamard(x, u, N):
	exp = 0
	for i in range(8):
		exp += b(x, i)*b(u, i)
	return ((-1)**exp)/N