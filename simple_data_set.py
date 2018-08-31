import numpy as np
prev = np.array([3,5])
arr = np.array([(3,5), (3,6), (2,6)])
print(prev)
print(arr[0])
t = arr[0] == prev
print(t.all())
if t.all():
    print("Something")

import numpy as np
import matplotlib.pyplot as plt

mean1 = [1,2]
cov1 = [[2,3],[3,1]]
x1, y1 = np.random.multivariate_normal(mean1, cov1, 5000).T

mean2 = [4,7]
cov2 = [[3,-0.5],[-0.5,2]]
x2, y2 = np.random.multivariate_normal(mean2, cov2, 5000).T

plt.plot(x1, y1, 'x', color='blue')
plt.plot(x2, y2, 'x', color='red')

plt.show()