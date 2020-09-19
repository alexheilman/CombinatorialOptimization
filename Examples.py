import numpy as np
from PruferCode import PruferCode

t = np.matrix([[0,1,0,0,0,1,1],\
			   [1,0,0,0,0,0,0],\
			   [0,0,0,0,0,0,1],\
			   [0,0,0,0,0,1,0],\
			   [0,0,0,0,0,1,0],\
			   [1,0,0,1,1,0,0],\
			   [1,0,1,0,0,0,0]])

A = PruferCode(t)
print(A)