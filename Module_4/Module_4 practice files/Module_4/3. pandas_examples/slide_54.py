import pandas, numpy

arr = numpy.array([10, 20, 30, 40, 50])
#series = pandas.Series(arr)
series = pandas.Series(arr, index=['a', 'b','c', 'd', 'a'])
print(series)