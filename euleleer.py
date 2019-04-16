import matplotlib.pyplot as plt
import math

h = 0.1
n= 10

arrayY = []
arrayX = []
f = lambda x0,y0: math.exp(-x0) + math.sin(y0)
y0 = 1
x0 = 0
arrayX.append(x0)
arrayY.append(y0)

for i in range(n):
    y1 = y0 + (f(x0, y0))*h
    y0 = y1
    x0 = x0 + h
    arrayX.append(x0)
    arrayY.append(y0)

print(arrayX , " ", arrayY)

print("X: ", x0)
print("Y: ", y0)

plt.plot(arrayX, arrayY,marker='o')
plt.show()
