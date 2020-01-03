import matplotlib.pyplot as plt

x = range(5)
y = [elem**2 for elem in x]

plt.plot(x, y)
plt.show()  # displays the plots