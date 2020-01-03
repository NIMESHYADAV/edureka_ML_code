# Histogram
# Histogram display's the distribution of a variable over a range of frequencies or values

import numpy
import matplotlib.pyplot as plt

y = numpy.random.randn(100, 100)
plt.hist(y, 5)
plt.show()

# 15 is bin size