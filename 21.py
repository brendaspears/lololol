import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure as fig

data = pd.read_csv("Data.csv")

mean = data['Litre'].mean()
std = data["Litre"].std()
median = data['Litre'].median()

q1 = np.percentile(data["Litre"], 25)
q2 = np.percentile(data["Litre"], 50)
q3 = np.percentile(data["Litre"], 75)

print(data["Litre"][1])
print("Mean: ", mean)
print("Standard Deviation: ", std)
print("Median: ", median)
print("Q1: ", q1)
print("Q3: ", q3)


# fig = plt.figure()
#
# fig.set_facecolor('lightgrey')
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

for i in range(0,15):
    plt.plot(1, data["Litre"][i], 'co')

y = [[] ,[],data["Litre"]]
my_xticks = ["Data", "Error Bar", "BoxPlot"]


plt.errorbar(2,mean, std, marker='s', ms=5, mew=2, solid_capstyle='round', capsize=5, color='black')
plt.text(2.05 , mean+std , "x + s = %.2f" % (mean+std))
plt.text(2.05 , mean, "x = %.2f" % (mean))
plt.text(2.05 , mean-std , "x - s = %.2f" % (mean-std))

plt.boxplot(y)

plt.xticks([1,2,3], my_xticks)
plt.text(3.2 , q1 , "Q1 = %.2f" % (q1))
plt.text(3.2 , q2 , "Q2 = %.2f" % (q2))
plt.text(3.2 , q3 , "Q2 = %.2f" % (q3))

# fig = plt.figure()

ax1.spines['bottom'].set_color('w')
ax1.spines['top'].set_color('w')
ax1.spines['right'].set_color('w')
ax1.spines['left'].set_color('w')
ax = plt.gca()
ax.grid(True, color='w', alpha=0.3)
ax1.set_facecolor('lightgrey')


plt.show()