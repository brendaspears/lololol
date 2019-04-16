import matplotlib.pyplot as plt
import math
import numpy as np

data = [5.5, 1.1, 6.5, 4.9, 6.4, 7.0, 1.5, 5.7, 5.9, 5.4, 6.1, 1.2, 7.3, 6.1, 4.4]
y = np.ones((len(data)), dtype=int)
print(y)
mean = np.mean(data)
std = np.std(data)
q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.5)
q3 = np.quantile(data, 0.75)

x = [[], [], data]

plt.plot(y, data, 'bo')
plt.errorbar(2, mean, std, marker='s', ms=5, capsize=5)
plt.boxplot(x)
plt.xticks([1,2,3],["Data", "Error Bar", "Boxplot"])

plt.show()