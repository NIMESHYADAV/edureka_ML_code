# Limiting the Axes: # Method 1: using axis()

import matplotlib.pyplot as plt

x = range(5)

# plots multiple figures using a single plot() function call.
plt.plot(x, [elem for elem in x],
         x, [elem*2 for elem in x],
         x, [elem*4 for elem in x])

plt.grid(True)

#axis([x_lower, x_upper, y_lower, y_upper])
plt.axis([-1, 5, -1, 10])
plt.show()