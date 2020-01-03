# Pie chart are used to compare multiple parts against the whole

import matplotlib.pyplot as plt
import numpy as np

# control colours
y = np.arange(1, 4)

plt.plot(y, '*', y*5, 'o', y*10, 'D', y*15, '^', y*20, 's')
plt.show()

