import numpy as np
from PruferCode import PruferCode
from AMfromPrufer import AMfromPrufer

M = np.matrix([[0,1,0,0,0,1,1],\
			   [1,0,0,0,0,0,0],\
			   [0,0,0,0,0,0,1],\
			   [0,0,0,0,0,1,0],\
			   [0,0,0,0,0,1,0],\
			   [1,0,0,1,1,0,0],\
			   [1,0,1,0,0,0,0]])

Prufer = PruferCode(M)

AM = AMfromPrufer(Prufer)


print(Prufer)
print(AM)

random.random()

def EulerianCircuit(matrix):
	t = 5