# Histogram
# Histogram display's the distribution of a variable over a range of frequencies or values

import numpy
import matplotlib.pyplot as plt

y = numpy.random.randn(100, 100)
print(y)
plt.hist(y)
plt.show()
