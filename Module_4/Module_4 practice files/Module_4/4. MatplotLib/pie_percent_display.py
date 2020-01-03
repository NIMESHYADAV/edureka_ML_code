import matplotlib.pyplot as plt

names = ['car', 'motorcycles', 'bike', 'electric-car']


fig1, ax1 = plt.subplots()
ax1.pie([20, 25, 40, 15],
        explode=(0, 0.1, 0, 0),
        labels=names,
        autopct='%1.1f%%'
)

ax1.axis('equal')
plt.show()
