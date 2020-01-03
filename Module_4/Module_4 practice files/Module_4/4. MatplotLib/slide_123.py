# control Line styling
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 100)

# specifying line styling : --(solid line), -.(solid-dash) & : (dotted)
plt.plot(y, '--', y*5, '-.', y*10, ':')

plt.show()

