import pandas as pd
import plotly.express as px

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

# Get death rate on years by race
race_death_rate = data.groupby(["year","race"],as_index=False).agg({"name":pd.Series.count})
race_death_rate.rename({"name":"deaths_count"},axis=1,inplace=True)
race_death_rate.head()

r_bar = px.bar(race_death_rate,
               x="year",
               y="deaths_count",
               color="race",
               title="deaths people over the years by race")
r_bar.update_layout(xaxis_title="year",
                    yaxis_title="deaths count")
r_bar.show()