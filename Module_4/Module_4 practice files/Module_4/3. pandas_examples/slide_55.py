import pandas as pd

# can we create a week day series like this? 1 - Sunday
# # from dict
data = {1: 'Sun', 2: 'Mon', 3: 'Tues'}
series = pd.Series(data)
print(series)


# DataFrame from a list
a = [11, 12, 13, 14]

df = pd.DataFrame(a)
print(df)
print(type(df))