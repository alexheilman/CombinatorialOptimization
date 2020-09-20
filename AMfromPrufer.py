'''
EXPLANATION
'''
import numpy as np

def AMfromPrufer(Prufer):				# Prufer code length (n-2), where n = # vertices
    A = Prufer							# A,B length = (n-1), because (n-1) edges in tree
    A.append(len(Prufer) + 2)			# A[n-1] last entry = largest vertex (Prufer length + 2)

    B = []
    for i in range(1, len(A)+1):		# Increment starting at 1. Smallest vertex is 1, not 0.
    	if i not in A:
    		B = [i]
    		break

    for i in range(1, len(A)):
    	for j in range(1, len(A)+1):		# Increment starting at 1. Smallest vertex is 1, not 0
    		if j not in A[i:] and j not in B:
    			B.append(j)
    			break
        
    AM = np.zeros((len(B)+1, len(B)+1))		# vertices 1 more than # edges
    for i in range(len(B)):
    	AM[A[i]-1, B[i]-1] = 1				# subtract one because indexing starts at 0.
    	AM[B[i]-1, A[i]-1] = 1				# subtract one because indexing starts at 0.
    
    return AM