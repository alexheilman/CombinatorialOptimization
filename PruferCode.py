'''
PruferCode function takes in any tree's adjacency matrix and returns its Prufer Code.
    Note:   Adjacency matrix must by a numpy matrix of size (n,n).
            Function limited to undirected graphs (two instances of every edge).

            Example Undirected Tree
                 (2)
                  |
                 (6)  (3)
                  |    |
            (1)--(0)--(5)--(4)

            Corresponding Adjacency Matrix
            AM = np.matrix([[0,1,0,0,0,1,1],\
                            [1,0,0,0,0,0,0],\
                            [0,0,0,0,0,0,1],\
                            [0,0,0,0,0,1,0],\
                            [0,0,0,0,0,1,0],\
                            [1,0,0,1,1,0,0],\
                            [1,0,1,0,0,0,0]])
'''
import numpy as np

def PruferCode(array):
    n = np.size(array,1)
    A = []
    B = []

    while np.sum(array) > 0:
        column_sums = np.sum(array, 0)
        for i in range(n):
            if column_sums[0, i] == 1:						    # identifies leaf nodes
                leaf = i                                        # trivial definition
                adjacent = np.where(array[:, i] == 1)[0][0]     # identify 
                A.append(leaf)                                  # A receives leaf node label
                B.append(adjacent)	                            # B receives adjacent node
                array[leaf, adjacent] = 0						# leaf node erased (both instances)
                array[adjacent, leaf] = 0                       # leaf node erased (both instances)
                break

    Prufer = B[:-1]
    return Prufer


