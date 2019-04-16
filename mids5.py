import math
import numpy as np
from sympy import *
import sympy as sym
import matplotlib.pyplot as plt


def trapezoidal(a, b, n, f):

    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    area = 0
    plt.plot(x,y)

    for i in range(n):
        area = area + (dx / 2) * (f(x[i]) + f(x[i + 1]))

    print("Area: ", area)
    return area


def integration(a, b):
    f = lambda x: 2 + sym.sin(x)
    x = symbols('x')
    e = integrate(f(x), x)
    ex = abs(e.subs(x, a) - e.subs(x, b))
    print("Real value: ", ex)
    return ex


f = lambda x: 2 + np.sin(x)
a = 0
b = np.pi/2
n = 2
error = ((integration(a, b) - trapezoidal(a, b, n, f))/integration(a, b))*100
print("Error: ", error)
print(trapezoidal(a, b, n, f))
plt.show()