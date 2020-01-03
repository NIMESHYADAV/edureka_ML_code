import numpy as np
arr = np.array([[11, 22, 33], [44, 55, 66], [1, 2,3]])

# append another array as row
new_arr = np.array([[10, 20, 30], [40, 50, 60]])
print(np.append(arr, new_arr, axis=0))  # axis=0 means row wise

# adding only a new row: be careful you nee

# wrong as both have different shape
#np.append(arr, [1,2,3], axis=0)

# correct
print(np.append(arr, [[1,2,3]], axis=0))

