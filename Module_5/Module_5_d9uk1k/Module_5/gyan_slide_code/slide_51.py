# correlation between GDP and Birth date
import pandas
import numpy
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
dataset = pandas.read_csv("AllCountries.csv")
selected_data = dataset.loc[:, ['Country', 'GDP', 'BirthRate']]
x = numpy.array(selected_data["GDP"])
y = numpy.array(selected_data['BirthRate'])
print(x, y)
plt.scatter(y, x)
#plt.xlim(0, 20000)
plt.show()
