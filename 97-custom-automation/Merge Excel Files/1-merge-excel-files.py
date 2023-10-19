import pandas as pd
from shutil import copyfile
import os
from openpyxl import load_workbook


template_file = 'template.xlsx'
output_file = 'merged.xlsx'
source_directory = 'source'

# Copy Contract_Template_EN.xlsx as Contract_1200_EN.xlsx
copyfile(template_file, output_file)

# get DataFrame for Contract template
contract_template = pd.ExcelFile(template_file)

# get worksheet names
contract_worksheets = contract_template.sheet_names

# Open Contract Excel spreadsheet in proper way, so that we can write to it without losing original data
contract_book = load_workbook(output_file)
writer = pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='overlay')
writer.sheets.update(dict((ws.title, ws) for ws in contract_book.worksheets))

# loop through every tab in Contract spreadsheet
for sheet_name in contract_worksheets:
    merged_frames = []
    for subdir, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".xlsx"):
                file_path = os.path.join(subdir, file)
                df = pd.read_excel(file_path, sheet_name)
                merged_frames.append(df)
    merged_df = pd.concat(merged_frames)
    merged_df.to_excel(writer, sheet_name, index=False)

# close the output file
writer.close()

