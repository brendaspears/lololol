import matplotlib.pyplot as plt


x = [1,2,3,4,5,6]
y = [4,5,6,7,2,3,4,4,4,6]
v = ["a" , "a" , "b" , "c" , "c" ,"c", "d", "a", "b", "b", "b","d"]
my_xticks = ["a", "b", "c", "d"]
plt.text(2.1 , 3.1 , "BITCH" )
plt.xticks([0,1,2,3], my_xticks)
plt.hist(v , 20)

plt.show()

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt
#
# x = [21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 31, 32, 33, 34, 35, 36, 37, 18, 49, 50, 100]
# num_bins = 5
# n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
# plt.show()