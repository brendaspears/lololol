import numpy as np
import math
from scipy.integrate import *
from sympy import *


a = 2
b = 1
f = lambda x : (2*x + 3/x)**2
areaG = quad(f, a, b)[0]
print("Gauss: ", areaG)

x = symbols('x')
inte = integrate(f(x))
intex = abs(inte.subs(x,a) - inte.subs(x, b))

print("Integrate: ", intex)