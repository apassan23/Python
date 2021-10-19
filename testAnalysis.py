import matplotlib.pyplot as plt
import numpy as np

x = np.array([45,55,65,75,85,95])
y = np.array([12, 10, 8, 7, 5, 2])

fontdict = {"family": "Rubik"}

plt.scatter(x, y)
plt.grid()
plt.xlabel("Marks Obtained out of 100", fontdict=fontdict)
plt.ylabel("Number of Students", fontdict=fontdict)
fontdict["color"] = "r"
plt.title("Scatter Diagram", fontdict=(fontdict))
plt.show()