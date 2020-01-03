import pandas
world_champions = {'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
           'ICC_rank': [2,3,7,8,4],
           'World_champions_Year': [2011,2015,1979,1992,1996],
           'Points':[874,787,753,673,855]}

chokers = {'Team': ['South Africa', 'New Zealand','Zimbabwe'],
           'ICC_rank': [1, 5, 9],
           'Points':[895,764,656]}

df1 = pandas.DataFrame(world_champions)
df2 = pandas.DataFrame(chokers)
print(df1)
print(df2)
print("#"*100)
# 1.Merge DFs
#print(pandas.merge(df1, df2, on='Team'))  # common data
#
# # 2. merge with Left Join i.e gets merged based on the keys from the left object
print(pandas.merge(df1, df2, on='Team', how='left'))
#
# # 3. merge with right join
#print(pandas.merge(df1, df2, on='Team', how='right'))
#
# 4. merge with outer join i.e gets merged based on full unions of the cols of both objects
#print(pandas.merge(df1, df2, on=['Team', 'ICC_rank'], how='outer'))
#
# 5. intersection of two dfs, inner
print(pandas.merge(df1, df2, on='Team', how='inner'))

#
