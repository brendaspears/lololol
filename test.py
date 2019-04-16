import numpy as np
import matplotlib.pyplot as plt

data = [5.5, 7, 6.1, 1.1, 1.5, 1.2, 6.5, 5.7, 7.3, 4.9, 5.9, 6.1, 6.4, 5.4, 4.4]

lowest = np.min(data)
highest = np.max(data)
middle = np.median(data)
arrayData = [lowest, middle, highest]
theData = [[],[],data]

plt.plot(1, [data], "ro")

plt.errorbar(2, [arrayData], marker = "o")

plt.boxplot(theData)

plt.xticks([1, 2, 3], ["Data", "Error Bar", "Box Plot"])

plt.show()