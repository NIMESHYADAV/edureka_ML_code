# Limiting the Axes 2:using xlim() and ylim()

import matplotlib.pyplot as plt

x = range(5)

# plots multiple figures using a single plot() function call.
plt.plot(x, [elem for elem in x],
         x, [elem*2 for elem in x],
         x, [elem*4 for elem in x])

plt.grid(True)

plt.xlim(-1, 5)
plt.ylim(-1, 10)
plt.show()
