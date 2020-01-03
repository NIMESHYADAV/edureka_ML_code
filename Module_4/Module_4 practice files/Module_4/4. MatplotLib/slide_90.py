# we can use NumPy to specify the values for both axes with greater precision


import numpy
import matplotlib.pyplot as plt

x = numpy.arange(0, 5, 0.01)
print(x)
y = [elem**2 for elem in x]
print(y)

plt.plot(x, y)
plt.show()  # displays the plot