import numpy

one_dim = numpy.zeros(8)
three_dim = one_dim.reshape((2,2,2))

# change it to 2d
#print(three_dim.reshape(4,2))

####
print(one_dim.reshape(8,1))