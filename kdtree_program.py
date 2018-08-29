import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# arr = np.array([(2,4), (7,1), (3,8), (6,1), (2,5), (6,6)])
arr = np.array([(3,5), (3,6), (2,6)])
print(np.median(arr[:, 0]))

class KDTree:
    def __init__(self, matrix, branch):
        self.left = None
        self.right = None
        print("Matrix shape: " + str(matrix.shape[0]))
               
        if matrix.shape[0] == 1:
            # self.node = np.median(matrix[:, branch])
            self.data = matrix[0]
            return
        if matrix.shape[0] == 0:
            return

        self.node = np.median(matrix[:, branch])
        print(np.median(matrix[:, branch]))

        left = []
        right = []

        for i in matrix[:, :]:
            if i[branch] <= self.node:
                left.append(i)
            else:
                right.append(i)

        self.left = KDTree(np.asarray(left), (branch + 1)%2)
        self.right = KDTree(np.asarray(right), (branch + 1)%2)

    
    def insert_data(self, root, matrix):
        #if array size is 1 then set data = array[0]
        #else perform another insert_data
        pass

tree = KDTree(arr, 0)
print("Yo")