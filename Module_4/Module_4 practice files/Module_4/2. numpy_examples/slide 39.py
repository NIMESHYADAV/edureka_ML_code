# arr[row_index, column_index]
# arr[row_slice, column_slice]

import numpy as np
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print(a)
print("#"*10)
print(a[0:2, 0:2])

# negative index

print(a[1,-1])  # gives last element of second row
"""
I understand sir, its about one dimension array,
can I print the array from third element
to last element by writing the range as arr[2:-1]
"""




