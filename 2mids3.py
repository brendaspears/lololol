import numpy as np
import math

def taylor_1(x, n):
    sum = 0
    for i in range(n):
        f = x**i
        sum = sum + f
    return sum

n = 5
x = 0.1
print("5: ",taylor_1(x, n))

n = 10
x = 0.1
print("10: ",taylor_1(x, n))
print("Error: ",(taylor_1(x, n)-taylor_1(x, n)))