import pandas as pd


extract = 'extract.xlsx'
template = 'template.xlsx'
diff_file = 'difference.xlsx'

my_list = [{
    'index_columns': 'Contract Display ID',
    'sheet_name':'Contract',
    'columns':['Contract ID'
              ,'Contract Display ID'
              ,'MLA Display ID'
              ,'Year'
              ,'Name'
              ,'Lease Type ID'
              ,'Currency ID'
              ,'Lease Area ID'
              ,'Lease Business Unit ID'
              ,'Company ID']
    },
    {
    'index_columns': 'Contract ID',
    'sheet_name':'Accounting',
    'columns':['Contract ID'
             ,'Contract Rate'
             ,'CPI ID'
             ,'Compounding Frequency ID'
             ,'Cost Center ID']
    }
]

writer = pd.ExcelWriter(diff_file, engine='openpyxl')

for my_item in my_list:
    first_xlsx = pd.read_excel(extract, sheet_name=my_item['sheet_name'])
    second_xlsx = pd.read_excel(template, sheet_name=my_item['sheet_name'])

    first_df = first_xlsx[my_item['columns']]
    first_df = first_df.set_index(my_item['index_columns'], drop=False)

    second_df = second_xlsx[my_item['columns']]
    second_df = second_df.set_index(my_item['index_columns'], drop=False)

    cols = second_df.columns

    merged = second_df.merge(first_df[cols], how='outer', left_index=True, right_index = True)

    left = merged.iloc[:, :len(cols)].set_axis(cols, axis=1)

    right = merged.iloc[:, len(cols):].set_axis(cols, axis=1)

    compared = left.compare(right, align_axis=0)

    compared.to_excel(writer, my_item['sheet_name'])

writer.close()
