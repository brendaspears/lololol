import numpy as np
import matplotlib.pyplot as plt

data = [5.5, 7, 6.1, 1.1, 1.5, 1.2, 6.5, 5.7, 7.3, 4.9, 5.9, 6.1, 6.4, 5.4, 4.4]

mean = np.mean(data)
std = np.std(data)
Dataa = [[],[],data]

Q1, Q2, Q3 = np.quantile(data, [.25, .50, .75])

plt.plot(1, [data], "co")

plt.text(2.05, mean + std, "x + s = %.2f" % (mean+std))
plt.text(2.05, mean, "x̄ = %.2f" % mean)
plt.text(2.05,mean-std, "x + s = %.2f" % (mean-std))
plt.errorbar(2, mean, std, capsize=5)

plt.boxplot(Dataa)
plt.text(3.2, Q3 - 0.15, "Q3 = %.2f" % Q3)
plt.text(3.2, Q2 - 0.15, "Q2 = %.2f" % Q2)
plt.text(3.2, Q1 - 0.15, "Q1 = %.2f" % Q1)

plt.xticks([1, 2, 3], ["Data", "Error Bar", "Box Plot"])

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# d = [5.5,7.0,6.1,1.1,1.5,1.2,6.5,5.7,7.3,4.9,5.9,6.1,6.4,5.4,4.4]
#
# mean = np.mean(d)
# std = np.std(d)
# print("Mean is = ",mean)
# print("Standard Deviation is = ",std)
#
# q1 = np.percentile(d,25)
# q2 = np.percentile(d,50)
# q3 = np.percentile(d,75)
#
# print("Q1 = ",q1, "Q2 = ",q2, "Q3 = ", q3)
#
# plt.xticks([1,2,3],["Data", "Error Bar", "Boxplot"] )
# #normal data plot
# plt.plot(1,[d],'co')
# #errorbar plot
# plt.text(2.05, mean+std,"x + s = %.2f" % (mean+std))
# plt.text(2.05, mean,"x = %.2f" % (mean))
# plt.text(2.05, mean-std,"x - s = %.2f" % (mean-std))
# plt.errorbar(2,mean,std,capsize=2,capthick=1,marker = 'o')
# #boxplot
# arrD = [[],[],d]
# plt.boxplot(arrD)
# plt.text(3.2, q3, "Q3 = %.2f"%(q3))
# plt.text(3.2, q2, "Q2 = %.2f"%(q2))
# plt.text(3.2, q1, "Q1 = %.2f"%(q1))
# plt.show()
#

