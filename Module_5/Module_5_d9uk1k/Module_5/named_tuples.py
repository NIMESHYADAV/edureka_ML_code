import collections

Edureka = collections.namedtuple('Edureka', 'name age gender')
print(Edureka) # this the named tuple

# how to put values to it
ravi = Edureka(age=25, name='Ravi', gender='M')
print(ravi.name)
print(ravi.age)
print(ravi[1]) # indexing also works