# concatenation is a process of combining two or more data structures.

import pandas
world_champions = {'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
           'ICC_rank':[2,3,7,8,4],
           'World_champions_Year':[2011,2015,1979,1992,1996],
           'Points':[874,787,753,673,855]}

chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
           'ICC_rank':[1,5,9],
           'Points':[895,764,656]}

df1 = pandas.DataFrame(world_champions)
df2 = pandas.DataFrame(chokers)
print(df1)
print(df2)
print("#"*50)
# M1
#print(pandas.concat([df1, df2]))

# M2
print(df1.append(df2))
