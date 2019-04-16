import matplotlib.pyplot as plt
import numpy as np
import math

data = [12.5, 11.4, 15.7, 13.1, 12.9, 14.1]

mean = np.mean(data)
std = np.std(data)

q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.5)
q3 = np.quantile(data, 0.75)

print("Mean: %.2f" % mean)
print("Standard Deviation: %.2f" % std)
print("Q1: ", q1)
print("Q2: ", q2)
print("Q3: ", q3)

x = [[],data]
plt.xlim(0, 3)
plt.errorbar(1, mean, std, capsize=5, marker='s', ms=5)
plt.boxplot(x)
plt.xticks([1, 2], ["Error Bar", "Boxplot"])
plt.text(1.1, mean+std, "Mean + STD: %.2f" % (mean+std))
plt.text(1.1, mean, "Mean: %.2f" % mean)
plt.text(1.1, mean-std, "Mean - STD: %.2f" % (mean-std))
plt.text(2.1, q1, "Q1: %.2f" % q1)
plt.text(2.1, q2, "Q2: %.2f" % q2)
plt.text(2.1, q3, "Q3: %.2f" % q3)
plt.show()
