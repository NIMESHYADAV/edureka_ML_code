
# 1.Loading excel sheet data into DataFrame

import pandas

table = pandas.read_excel(path)
print(table)


# 2. Exporting DataFrame to excel spreadsheet.

table.to_csv(output_path)

