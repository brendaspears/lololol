import numpy as np
import matplotlib.pyplot as plt

data = [12.5, 11.4, 15.7, 13.1, 12.9, 14.1]

mean = np.mean(data)
std = np.std(data)
print("Mean: %.2f" % mean)
print("Standard Deviation: %.2f" % std)
#
# q1 = np.quantile(data, .25)
# q2 = np.quantile(data, .50)
# q3 = np.quantile(data, .75)
q1, q2, q3 = np.quantile(data, [.25, .50, .75])

print("Q1: %.2f" % q1)
print("Q2: %.2f" % q2)
print("Q3: %.2f" % q3)

x = ([], data)

plt.errorbar(1, mean, std, marker='s', capsize=5, mew=2 )
plt.text(1.05, mean+std, "Mean + std: %.2f" % (mean+std))
plt.text(1.05, mean, "Mean: %.2f" % (mean))
plt.text(1.05, mean-std, "Mean - std: %.2f" % (mean-std))

plt.boxplot(x)
plt.xticks([1, 2], ["Error Bar", "Boxplot"])
plt.show()
