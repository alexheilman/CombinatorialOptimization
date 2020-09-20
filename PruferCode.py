'''
PruferCode function takes in any tree's adjacency matrix and returns its Prufer Code.
    Note:   Adjacency matrix must by a numpy matrix of size (n,n).
            Function limited to undirected graphs (two instances of every edge).

            Example Undirected Tree
                 (3)
                  |
                 (7)  (4)
                  |    |
            (2)--(1)--(6)--(5)

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

    while np.sum(array) > 2:                                    # stop with one pair left
        column_sums = np.sum(array, 0)                          # column sum = # edges per node
        for i in range(n):
            if column_sums[0, i] == 1:						    # identifies leaf nodes
                leaf = i                                        # trivial definition
                parent = np.where(array[:, i] == 1)[0][0]       # identify parent node
                B.append(leaf + 1)                              # A receives leaf   (+1 bc indexing)
                A.append(parent + 1)	                        # B receives parent (+1 bc indexing)
                array[leaf, parent] = 0						    # leaf node erased  (both instances)
                array[parent, leaf] = 0                         # leaf node erased  (both instances)
                break

    Prufer = A
    return Prufer


