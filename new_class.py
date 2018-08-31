class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def print_data(self):
        print(self.data)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.print_data()

n1.left = n2
n2.right = n3

print(n1.left)
print(n2)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#arr = np.array([[(2,4), (7,1), (3,8), (6,1), (2,5), (6,6), (10,9)]])
#print(arr)
arr = np.array([(2,4)])
print(arr.shape[0])
mid = np.median(arr[:, 0])
print(np.median(arr[:, 1]))
# print(arr[:mid, 0])
# print(np.median(arr))

import numpy as np
from sklearn.neighbors import KDTree
arr = np.array([(1,7), (1,6), (6,6), (6,6)])
new_tree = KDTree(arr, leaf_size = 1)
print("Done")

import numpy as np
from scipy.spatial import cKDTree
#arr = np.array([(1,7), (1,6), (6,6), (6,6)])
arr = np.array([(3,5), (3,6), (2,6)])
tree = cKDTree(arr, 1)