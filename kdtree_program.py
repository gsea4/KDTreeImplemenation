import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

arr = np.array([[1,9],[9,3],[4,1],[3,7],[5,4],[6,8],[7,2],[8,8],[7,9],[9,6]])

def divide(arr, branch):
    mid = int(np.ceil(len(arr)/2))
    left = np.array([[]])
    right = np.array([[]])
    
    for i in arr[:mid]:
        if i[branch] < arr[mid,0]:
            print(i)
            np.append(left,[i])
        else:
            np.append(right, i)

    for i in arr[mid:]:
        if i[branch] >= arr[mid,0]:
            np.append(right, i)

        else:
            np.append(left,i)

    print(left)
    print(right)


divide(arr, 0)