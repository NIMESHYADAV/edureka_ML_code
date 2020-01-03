# adding a grid in the graph

import matplotlib.pyplot as plt

x = range(5)

# plots multiple figures using a single plot() function call.
plt.plot(x, [elem for elem in x],
         x, [elem*2 for elem in x],
         x, [elem*4 for elem in x])

plt.grid(True)
plt.show()