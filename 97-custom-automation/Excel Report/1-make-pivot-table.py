import pandas as pd

# Read Excel File
df = pd.read_excel('supermarket_sales.xlsx')
# Select columns: 'Gender', 'Product line', 'Total'
df = df[['Gender', 'Product line', 'Total']]
# Create a Pivot Table
pivot_table = df.pivot_table(index='Gender', columns='Product line',
                             values='Total', aggfunc='sum').round(0)

