import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# arr = np.array([(2,4), (7,1), (3,8), (6,1), (2,5), (6,6)])
# arr = np.array([(1,4), (1,6), (6,6)])
# arr = np.array([(4,7), (3,6), (3,6)])
# arr = np.array([(3,5), (3,6), (2,6)])
# arr = np.array([(6,1), (7,1), (6,6)])
arr = np.array([(1,1),(1,1), (2,3)])
print(np.median(arr[:, 0]))

class KDTree:
    def __init__(self, matrix, branch, dimension):
        self.left = None
        self.right = None
        # print("Matrix shape: " + str(matrix.shape[0]) + " " + str(matrix.shape))
               
        if matrix.shape[0] == 1:
            self.data = matrix[0]
            return
        if matrix.shape[0] == 0:
            return

        self.node = np.median(matrix[:, branch])

        left = []
        right = []
        for i in matrix[:, :]:
            if i[branch] <= self.node:
                left.append(i)
            else:
                right.append(i)

        if len(left) == matrix.shape[0] or len(right) == matrix.shape[0]:
            prev = np.array([])
            for i in matrix[:, :]:
                isDuplicated = np.array_equal(i, prev)
                prev = i
            
            if isDuplicated:
                self.left = matrix
                return
            
            left = []
            right = []
            for i in matrix[:, :]:
                if i[branch] < self.node:
                    left.append(i)
                else:
                    right.append(i)

        self.left = KDTree(np.asarray(left), (branch + 1) % dimension, dimension)
        self.right = KDTree(np.asarray(right), (branch + 1) % dimension, dimension)

tree = KDTree(arr, 0, arr.shape[1])
print("Yo")