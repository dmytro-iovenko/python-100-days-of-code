import pandas as pd

# Load the data
df_data = pd.read_csv('mission_launches.csv')

# Get the shape
print("The shape of the data is: ",df_data.shape) # Gives shape of data

# Get number of rows and columns
count_row = df_data.shape[0]  # Gives number of rows
count_col = df_data.shape[1]  # Gives number of columns
print("There are ", count_row, " rows and ", count_col, " columns in this data.")

# Get column names
print("The column names are as follows: ",df_data.columns)

# Check for NaN values or duplicates
df_data.isna()

# Remove columns with junk data
df_data = df_data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)

# Clean duplicates
df_data = df_data.drop_duplicates()

# Change the name of a column
df_data = df_data.rename({'Detail': 'Launches'}, axis=1)
