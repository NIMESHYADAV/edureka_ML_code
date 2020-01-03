import numpy as np
arr = np.arange(23, 50, 2)
print(arr)
arr_slice = slice(1, 10, 2)  #these numbers are indexes
print(arr[arr_slice])
# also
print(arr[1:5:3])  # start, stop, step
