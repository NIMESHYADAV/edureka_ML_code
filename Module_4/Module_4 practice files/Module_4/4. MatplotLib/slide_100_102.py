# Adding labels using xlabel() and ylabel()
# adding title using title()

import matplotlib.pyplot as plt

x = range(5)

# plots multiple figures using a single plot() function call.
plt.plot(x, [elem for elem in x],
         x, [elem*2 for elem in x],
         x, [elem*4 for elem in x])

plt.grid(True)

# adding label
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# adding Title
plt.title('Polynomial Graph')
plt.show()
