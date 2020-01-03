import pandas as pd

world_cup = {'Team':['West Indies','West indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,1],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}

df = pd.DataFrame(world_cup)
grouped = df.groupby('Team')
print(grouped)

# Iteration
for name, group in grouped:
    print(name)
    print(group)
    print("#"*30)