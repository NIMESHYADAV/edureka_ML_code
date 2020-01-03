# DataFrame addition and deletion of columns

import pandas

data = {'one': pandas.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pandas.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
table = pandas.DataFrame(data)

# adding a new column to an existing DataFrame
table['three'] = pandas.Series([10, 20, 30], index=['a', 'b', 'c'])
print(table)
print("#"*20)
# DataFrame Column deletion
# Method 1:  DataFrame columns can be deleted using the del() function.
# del table['one']
# print(table)
#
# # Method 2: DataFrame columns can be deleted using the pop() function.
# table.pop('one')
# print(table)

# DataFrame rows can be selected by passing the row label to the loc() function
#print(table.loc['c'])  # Series object

# # DatFrame rows can also be selected by passing the row index to the iloc() function

print(table.iloc[2])




