
# 1.Loading CSV data into DataFrame

import pandas

path = r"/Users/gyanendra/Desktop/PyDataScience_venv/Module4/574_m4_datasets_v3.0/BigMartSalesData.csv"
table = pandas.read_csv(path)
#print(table)


# 2. Exporting data from DataFrame to csv file

table.to_csv('export.csv', index=False)
#
# # 3. Loading excel sheet in pandas

