import numpy as np
import scipy as sp
import math
from scipy.spatial import distance
import matplotlib.pyplot as plt

# arr = np.array([(2,4), (7,1), (3,8), (6,1), (2,5), (6,6)])
# arr = np.array([(1,9), (2,3), (4,1), (3,7), (5,4), (6,8), (7,2), (8,8), (7,9), (9,6)])
# arr = np.array([(1,4), (1,6), (6,6)])
# arr = np.array([(4,7), (3,6), (3,6)])
# arr = np.array([(3,5), (3,6), (2,6)])
# arr = np.array([(6,1), (7,1), (6,6)])
# arr = np.array([(1,1),(1,1), (2,3)])

arr = np.array([(1, 3), (1, 8), (2, 2), (2, 10), (3, 6), (4, 1), (5, 4), (6, 8), (7, 4), (7, 7), (8, 2), (8, 5), (9, 9),(6,8)])
target = np.array((4,8))
closest = math.inf

class KDTree:
    def __init__(self, matrix, branch, dimension):
        if(matrix.size == 0):
            return
        
        self.split = branch
        self.left = None
        self.right = None
               
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
                isIdentical = np.array_equal(i, prev)
                prev = i
            
            if isIdentical:
                self.data = matrix
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

    def find_nearest(self, vector):
        global closest
        self.closest_point = None

        if hasattr(self, 'data'):
            if self.data.ndim > 1:
                temp = distance.euclidean(self.data[0], vector)
            else:
                temp = distance.euclidean(self.data, vector)
            if temp < closest:
                closest = temp
                return self.data
            else:
                return

        if self.split == 0 and hasattr(self, 'node'):
            n = np.array((self.node,vector[1]))
            self.distance_from_target = distance.euclidean(n, vector)
        elif self.split == 1 and hasattr(self, 'node'):
            n = np.array((vector[0], self.node))
            self.distance_from_target = distance.euclidean(n, vector)

        if vector[self.split] <= self.node and self.left:
            self.search_first = 'left'
            self.closest_point = self.left.find_nearest(vector)
        elif vector[self.split] > self.node and self.right:
            self.search_first = 'right'
            self.closest_point = self.right.find_nearest(vector)

        if hasattr(self, 'distance_from_target'):
            if self.closest_point is not None:
                self.t = self.closest_point
            if self.search_first == 'left' and self.distance_from_target < closest:
                self.closest_point = self.right.find_nearest(vector)
            elif self.search_first == 'right' and self.distance_from_target < closest:
                self.closest_point = self.left.find_nearest(vector)
            if hasattr(self, 't') and self.closest_point is None:
                self.closest_point = self.t
        return self.closest_point

tree = KDTree(arr, 0, arr.ndim)
result = tree.find_nearest(target)
print("Result: \n" + str(result))
print("Distance: " + str(closest))
