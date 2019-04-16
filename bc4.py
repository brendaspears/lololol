import numpy as np
from scipy.integrate import odeint
import math
import matplotlib.pyplot as plt

def rk6(f,y0,x):
    h = x[1] - x[0]; n = len(x)
    y = np.zeros(n)
    y[0] = y0
    s21 = np.sqrt(21.0)
    for i in range(n - 1):
        k1 = h * f( x[i], y[i] )
        k2 = h * f( x[i] + h, y[i] + k1 )
        k3 = h * f( x[i] + h/2, y[i] + (3*k1 + k2)/8 )
        k4 = h * f( x[i] + 2*h/3, y[i]+ (8*k1 + 2*k2 + 8*k3)/27)
        k5 = h * f( x[i] + (7 - s21)*h/14, y[i] + (  3*(3*s21 - 7)*k1 - 8*(7 - s21)*k2 + 48*(7 - s21)*k3 - 3*(21 - s21)*k4)/392)
        k6 = h * f( x[i] + (7 + s21)*h/14, y[i] + ( -5*(231 + 51*s21)*k1 - 40*(7 + s21)*k2 - 320*s21*k3 + 3*(21 + 121*s21)*k4 + 392*(6 + s21)*k5 )/1960)
        k7 = h * f( x[i] + h, y[i] + ( 15*(22 + 7*s21)*k1 + 120*k2 + 40*(7*s21 - 5)*k3 - 63*(3*s21 - 2)*k4 - 14*(49 + 9*s21)*k5 + 70*(7 - s21)*k6)/180)
        y[i+1] = y[i] + ( 9*k1 + 64*k3 + 49*k5 + 49*k6 + 9*k7 )/180
    return y


f = lambda x,y : np.exp(-x) + np.sin(y)
y0 = np.array([1]); x = np.linspace(0.0, 1.0, 11)
y_rk6 = rk6(f, y0, x)
y_python = odeint(f, y0, x)
fig = plt.figure()
ax = fig.add_subplot(2,3,2)
ax.plot(x, y_rk6, label = 'RK6')
ax.plot(x, y_python, label = 'Scipy')
ax.legend()
print('*** See Figure 100. I guess something is wrong with the formulas.')