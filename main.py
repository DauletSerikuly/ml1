import numpy as np

X = np.random.normal(loc=10, scale=10, size=(100, 10))


mean = np.mean(X, axis=0)
sko = np.std(X, axis=0)
normX = ((X - mean)/sko)
print(normX)

Z = np.array([[4, 5, 0],
 [1, 9, 3],
 [5, 1, 1],
 [3, 3, 3],
 [9, 9, 9],
 [4, 7, 1]])
r = np.sum(Z, axis=1)
print(np.nonzero(r > 10))

A = np.eye(3)
B = np.eye(3)
print(A)
13
print(B)
AB = np.vstack((A, B))
print(AB)
