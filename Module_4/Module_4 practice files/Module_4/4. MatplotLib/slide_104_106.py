# Adding legends using legend()
# saving the plot using savefig()

import numpy
import matplotlib.pyplot as plt

x = numpy.arange(5)

# plots multiple figures using a single plot() function call.
plt.plot(x, x, label='linear')
plt.plot(x, x*x, label='square')
plt.plot(x, x*x*x, label='cube')

plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polynomial Graph')
plt.legend() # displays legend on the plot
plt.savefig('plot.png') # saves the plot

plt.show()
