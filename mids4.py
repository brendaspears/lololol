import matplotlib.pyplot as plt
import numpy as np
import math

# arrX = []
# arrY = []
# y0 = 1
# x0 = 0
# f = lambda x0, y0 : np.exp(-x0) + np.sin(y0)
# arrX.append(x0)
# arrY.append(y0)
#
# n = 10
# h = 0.1
#
# for i in range(n):
#     y1 = y0 + f(x0,y0)*h
#     y0 = y1
#     x0 = x0 + h
#     arrX.append(x0)
#     arrY.append(y0)
#
#
# print(x0)
# print(y0)
# plt.plot(arrX, arrY)
# plt.show()

def func(x0,y0):
    f = lambda x0, y0: np.exp(-x0) + np.sin(y0)
    return f(x0,y0)

def euler(h, n):
    arrX = []
    arrY = []
    y0 = 1
    x0 = 0
    arrX.append(x0)
    arrY.append(y0)

    for i in range(n):
        y1 = y0 + (func(x0,y0))*h
        y0 = y1
        x0 = x0 + h
        arrX.append(x0)
        arrY.append(y0)

    print(x0)
    print(y0)
    plt.plot(arrX, arrY)
    plt.show()

n = 10
h = 0.1
euler(h, n)