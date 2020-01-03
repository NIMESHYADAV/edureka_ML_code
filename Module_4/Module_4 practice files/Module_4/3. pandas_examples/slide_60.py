# creating a data frame

# Method1: from a list

import pandas

mylist = [11, 22, 33, 44]
table = pandas.DataFrame(mylist)
print(table)
print(type(table))
