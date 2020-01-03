# Bar chart
# bar charts used to compare two or more values using rectangular bars

import matplotlib.pyplot as plt

dictionary = {'A': 25, 'B': 70, 'C': 55, 'D': 90}

for i, key in enumerate(dictionary):
    plt.bar(i, dictionary[key])
plt.show()

# each key-value pair is plotted individually