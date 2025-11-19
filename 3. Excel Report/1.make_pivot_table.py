import pandas as pd
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths for input and output files
input_path = os.path.join(script_dir, 'supermarket_sales.xlsx')
output_path = os.path.join(script_dir, 'pivot_table.xlsx')

# Read Excel File
df = pd.read_excel(input_path)
# print(df)

# Select columns: 'Gender', 'Product line', 'Total'
df = df[['Gender', 'Product line', 'Total']]
# print(df)

# Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line',
                             values='Total', aggfunc='sum').round(0)
# print(pivot_table)

# Export pivot table to Excel file
pivot_table.to_excel(output_path, 'Report', startrow=4)

print('done')

