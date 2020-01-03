# Multiline plots: Line plots
# multiple functions can be drawn on the same plot by giving multiple call to plot() before show()

import matplotlib.pyplot as plt

x = range(5)
plt.plot(x, [elem for elem in x])
plt.plot(x, [elem*elem for elem in x])
plt.plot(x, [elem*elem*elem for elem in x])
plt.show()

# Three different line plots with different colours
