# creating a DataFrame from a list of dicts and accompanying row indices

# Method2: from a list of dictionaries.

import pandas

data = [{'a': 1, 'b': 2}, {'a': 2, 'b': 4, 'c': 8}]
table = pandas.DataFrame(data, index=['first', 'second']) # explicitly giving indexes
print(table)

