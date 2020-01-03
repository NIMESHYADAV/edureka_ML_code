# Row addition
# append() function can be used to add more rows to the DataFrame.


import pandas

data = {'one': pandas.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pandas.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
table = pandas.DataFrame(data)

# adding a new column
table['three'] = pandas.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Original DataFrame")
print(table)

# Method2: Adding a new rows from an existing DF
row = pandas.DataFrame([[11, 13], [17, 19]], columns=['two', 'three'])

print("DataFrame to be appended")
print(row)
table = table.append(row)
print("Appended DF")
print(table)

# drop() function to drop rows by passing the index of the row.
table = table.drop('a')
print(table)
