# creating a data frame

# Method2: from a list of dictionaries.

import pandas

data = [{'a': 1, 'b': 2}, {'a': 2, 'b': 4, 'c': 8}]
table = pandas.DataFrame(data)  # dict keys would be the column names
print(table)

