import numpy as np

arr = np.genfromtxt('my_file.csv', delimiter=',', dtype=int)
print(arr)
np.savetxt('out.csv', arr, fmt='%.4e')