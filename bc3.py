import numpy as np
from scipy.linalg import solve

# a = np.array([[3, 1, 0, 0], [2, 3, 2, 0], [1, 2, 4, 1], [0, 1, 1, 2]])
# b = np.array([[1], [1], [1], [1]])
# x = solve(a,b)
# print(a)
# print(b)
# print(x)
# detA = np.linalg.det(a)
# print(detA)
# normB = np.linalg.norm(b)
# print(normB)

A = np.array([[3.0, 1.0, 0.0, 0.0],
              [2.0, 3.0, 2.0, 0.0],
              [1.0, 2.0, 4.0, 1.0],
              [0.0, 1.0, 1.0, 2.0]])
b = np.matrix([ [1.0], [1.0], [1.0], [1.0] ] )
x = np.linalg.solve(A, b)
print( 'The solution vector x = {0}'.format(x.transpose()) )
print( 'The det(A) = {0}'.format( np.linalg.det(A)))
print( 'The norm(b) = {0}'.format( np.linalg.norm(b)))