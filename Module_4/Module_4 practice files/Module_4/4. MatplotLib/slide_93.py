# Multiline plots: Line plots
# multiple functions can be drawn on the same plot in single plot() call.

import matplotlib.pyplot as plt

x = range(5)

# plots multiple figures using a single plot() function call.
plt.plot(x, [elem for elem in x], x, [elem*elem for elem in x], x, [elem*elem*elem for elem in x])
plt.show()

# Three different line plots with different colours
