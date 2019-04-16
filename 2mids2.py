import numpy as np
import math

A = np.array([[6, 2, 0, 0, 0],
    [-1, 7, 2, 0, 0],
    [0, -2, 8, 2, 0],
    [0, 0, 3, 7, -2],
    [0, 0, 0, 3, 5]])

b = np.array([[2],
             [-3],
             [4],
             [-3],
             [1]])

ta = np.transpose(A)
tb = np.transpose(b)
print("Transpose: ", ta)
print("Transpose: ", tb)
x = np.linalg.solve(A,b)
n = np.linalg.norm(x)
print("Norm: ", x)