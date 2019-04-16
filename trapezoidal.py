import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from scipy.integrate import *
from sympy import *

# f = lambda x : x**2 + 3*x + 5
# f = lambda x : x**2 + 3
f = lambda x : 2*x**3 + 4*x**2 + 5
# f = lambda x : 3*(x+5)**2 + 3*x
# f = lambda x : 3*(x+5)**2 + 3*(x-5)


a = 1; b = 5; N = 100
# a = -2; b = 8; N = 100
# a = 2; b = 100; N = 100


# a = 0; b = 5; N = 100
n = 10

x = np.linspace(a, b, N+1)
y = f(x)
dx = (b-a)/N

X = np.linspace(a, b, n*N+1)
Y = f(X)
plt.plot(X,Y)

area = 0

for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    area = area + (dx/2)*(f(x[i])+f(x[i+1]))
    ys = [0, f(x[i]), f(x[i+1]),0]
    plt.fill(xs, ys, 'b', edgecolor = 'b', alpha = 0.2)

x = symbols('x')
e = integrate(f(x))
ex = abs(e.subs(x,a)-e.subs(x,b))
print("Real value: ",ex)


areaG = quad(f,a,b)[0]
print("error: " ,ex - areaG)

print("Gauss: ",areaG)
print("\n Approximated Area = %.2f" % (area))
plt.title("Trapezoidal Rule, N = {}".format(N))
plt.show()
