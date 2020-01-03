import pandas as pd
dataset = pd.read_csv("AllCountries.csv")
selected_data = dataset.loc[:, ['Country', 'LandArea']]
#print(selected_data)
for i in selected_data.itertuples():
    if i.LandArea > 2000: # i[2] or i.LandArea
        print(i.Country)