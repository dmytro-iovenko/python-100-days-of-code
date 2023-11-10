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

# Get death rate on years by gender
gender_death_rate = data.groupby(["year","gender"],as_index=False).agg({"name":pd.Series.count})
gender_death_rate.rename({"name":"deaths_count"},axis=1,inplace=True)
gender_death_rate.head()

g_bar = px.bar(gender_death_rate,
               x="year",
               y="deaths_count",
               color="gender",
               title="deaths people over the years by gender",
               barmode="group")
g_bar.update_layout(xaxis_title="year",
                    yaxis_title="deaths count")
g_bar.show()

# Get death rate on years by age
age_death_rate = data.groupby(["year","age"],as_index=False).agg({"name":pd.Series.count})
age_death_rate.rename({"name":"deaths_count"},axis=1,inplace=True)
age_death_rate.head()

a_bar = px.bar(age_death_rate,
               x="year",
               y="deaths_count",
               color="age",
               title="deaths people over the years by age")
a_bar.update_layout(xaxis_title="year",
                    yaxis_title="deaths count")
a_bar.show()

# Get death rate on years by city and state
state_city_deaths = data.groupby(["state","city"],as_index=False).agg({"name":pd.Series.count})
state_city_deaths.rename({"name":"deaths_count"},axis=1,inplace=True)
state_city_deaths.head()

a_sun = px.sunburst(state_city_deaths,
               names="city",
               parents="state",
               values="deaths_count",
               title="deaths people over the years by city and state")
a_sun.show()

# Count people who killed was armed
is_armed = data.value_counts("armed")
is_armed.head()

a_pie = px.pie(names=is_armed.index,
               values=is_armed.values,
               title="was people who killed armed?")
a_pie.show()