import numpy as np
import matplotlib.pyplot as plt

mean1 = [1,2]
cov1 = [[2,3],[3,1]]
dataset0 = np.random.multivariate_normal(mean1, cov1, 5000)
x1, y1 = np.random.multivariate_normal(mean1, cov1, 5000).T

mean2 = [4,7]
cov2 = [[3,-0.5],[-0.5,2]]
x2, y2 = np.random.multivariate_normal(mean2, cov2, 5000).T
dataset1 = np.random.multivariate_normal(mean1, cov1, 5000)

X = np.vstack((dataset0, dataset1))

y_raw = np.append(np.zeros(5000, dtype='int64'), np.ones(5000, dtype='int64'))
y = y_raw[:, np.newaxis]


plt.plot(x1, y1, 'x', color='blue')
plt.plot(x2, y2, 'x', color='red')

#plt.show()
import numpy as np
mask = np.random.rand(10000) < 0.8

y_mask = mask[:, np.newaxis]

training_data = y[y_mask]
trainging_label = X[mask]

print(training_data.shape)
print(trainging_label.shape)