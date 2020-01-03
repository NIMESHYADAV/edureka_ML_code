# control colours
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 3)
plt.plot(y, 'y')  # specifying line colours: 'y' : yellow
plt.plot(y+5, 'm') # 'm' for magenta
plt.plot(y+10, 'c') # 'c' cyan

plt.show()

