# GDPs of ten richest countries

import pandas
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
dataset = pandas.read_csv("AllCountries.csv")
selected_data = dataset.loc[:, ['Country', 'GDP', 'BirthRate']]
#print (dataset.iloc[:, 1]) # access columns via Index Location iloc
#
sorted_data = selected_data.sort_index(by='GDP', ascending=False)  # sort the data
selected_sorted_data = sorted_data.iloc[:10] # select first 10 rows of sorted dataset
print(selected_sorted_data)
plt.pie(selected_sorted_data['GDP'], labels=selected_sorted_data['Country'])
plt.show()
