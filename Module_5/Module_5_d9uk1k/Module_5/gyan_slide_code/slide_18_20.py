import pandas as pd

world_cup = {'Team': ['West Indies','West indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
           'Rank': [7,7,2,1,6,4,1,1,1,2,1],
           'Year': [1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df = pd.DataFrame(world_cup)
print(df)
print("#"*40)

# # group by based on single column
# print(df.groupby('Team').groups)
#
# group by based on multiple column
print(df.groupby(['Team', 'Rank']).groups)