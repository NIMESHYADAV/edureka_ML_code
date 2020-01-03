# scatter plot
# displays values for two sets of data, visualize as a collection of points
import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(1000)
y = np.random.rand(1000)
plt.scatter(x, y)

plt.show()

