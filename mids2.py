import math
import numpy as np

def mycos(x,n):
    sum = 0
    for i in range(n+1):
        f = (((-1)**i)*((8*x)**(2*i)))/math.factorial(2*i)
        sum = sum + f
    return sum


x = (3/8) * math.pi
n = 20
print("Sum: ", mycos(x,n))
