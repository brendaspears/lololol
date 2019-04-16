import numpy as np
import math as m

def mycos(x, n):
    total = 0
    for i in range( n ):
        total = total + (-1)**i * (8*x)**(2*i) / m.factorial(2*i)
    return total

x = 3/8*np.pi; n = 20
print('Numpy result = {0}'.format( np.cos(8.0*x) ) )
print('Mycos result = {0}'.format( mycos(x, n) ) )





