import numpy as np

arr = np.loadtxt('filex.txt', dtype=int)
print(arr)

# # transfer array to a file
#
#np.savetxt('output_array.txt', arr, fmt="%1.1e")
np.savetxt('output_array.txt', arr, fmt="%1.2e", delimiter='$')
#print(np.savetxt.__doc__) # to see documentation