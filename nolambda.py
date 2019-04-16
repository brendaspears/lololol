import matplotlib.pyplot as plt
import math

h = 0.1
n= 10

arrayY = []
arrayX = []

y0 = 1
x0 = 0
f = math.exp(-x0) + math.sin(y0)

arrayX.append(x0)
arrayY.append(y0)

for i in range(n):
    y1 = y0 + (f)*h
    y0 = y1
    x0 = x0 + h
    arrayX.append(x0)
    arrayY.append(y0)
    f = math.exp(-x0) + math.sin(y0)

print(arrayX)
print(arrayY)
print("X: ", x0)
print("Y: ", y0)

plt.plot(arrayX, arrayY,marker='o')
plt.show()
