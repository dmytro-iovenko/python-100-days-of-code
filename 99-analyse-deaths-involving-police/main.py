import pandas as pd

# Load the Data
data = pd.read_csv("deaths_by_police.csv")

# Preliminary Data Exploration
print(data.shape)
data.head()

# Check for Missing Values and Duplicates
print(data.isna().values.any())
data.duplicated().values.any()

print(data.shape)
data.head()

# Converting date column to datetime index
data["date"] = pd.DatetimeIndex(data["date"]).year
data.rename(columns = {'date':'year'}, inplace = True)

data.info()