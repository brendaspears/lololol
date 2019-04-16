import numpy as np
import math
from scipy.linalg import*

A = np.array([[3, 1, 0, 0], [2, 3, 2, 0], [1, 2, 4, 1], [0, 1, 1, 2]])
b = np.array([[1], [1], [1], [1]])
x = solve(A, b)
print("a. ", x)
detA = np.linalg.det(A)
print("b. ", detA)
normB = np.linalg.norm(b)
print("c. ", normB)