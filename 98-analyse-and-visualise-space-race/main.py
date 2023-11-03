import pandas as pd
import plotly.express as px
import iso3166 as iso
import matplotlib.pyplot as plt

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


# Descriptive statistics
df_data.info()

df_data.describe()

df_data[df_data["Price"].notna()]["Price"].str.replace(',', '').astype(float).describe()

# Extracting data from the Date column
df_data['Year'] = pd.to_datetime(pd.to_datetime(df['Date'], utc=True).dt.strftime('%Y'))
df_data['Year_and_Month'] = pd.to_datetime(pd.to_datetime(df['Date'], utc=True).dt.strftime('%Y-%m'))

df_data['Year_number'] = pd.to_datetime(df['Date'], utc=True).dt.year
df_data['Month_name'] = pd.to_datetime(df['Date'], utc=True).dt.month_name()
df_data['Month_number'] = pd.to_datetime(df['Date'], utc=True).dt.month

# Create a chart that shows the number of space mission launches by organisation.
df_data['Organisation'].value_counts().plot()

# Get number of active vs retired rockets
df_data["Rocket_Status"].value_counts()
df_data["Rocket_Status"].value_counts().sort_values().plot(kind="barh")

# How many missions were successful?
df_data["Mission_Status"].value_counts()

# How many missions failed?
df_data.groupby("Mission_Status").agg({"Mission_Status":pd.Series.count})

# Get a histogram and visualise the distributio
px.histogram(df_data.sort_values(by=["Organisation", "Price"], ascending=[False, False]), x="Price",nbins=10) 

# Show the number of launches by country
f_data["Country"] = df_data["Location"].str.split(", ").str[-1]

df_data.loc[(df_data["Country"] == 'Russia'), "Country"] = "Russian Federation"
df_data.loc[(df_data["Country"] == 'New Mexico'), "Country"] = "USA"
df_data.loc[(df_data["Country"] == 'Yellow Sea'), "Country"] = "China"
df_data.loc[(df_data["Country"] == 'Shahrud Missile Test Site'), "Country"] = "Iran"
df_data.loc[(df_data["Country"] == 'Pacific Missile Range Facility'), "Country"] = "USA"
df_data.loc[(df_data["Country"] == 'Barents Sea'), "Country"] = "Russian Federation"
df_data.loc[(df_data["Country"] == 'Gran Canaria'), "Country"] = "USA"
df_data.loc[(df_data["Country"] == 'Iran'), "Country"] = "Iran, Islamic Republic of"
df_data.loc[(df_data["Country"] == 'South Korea'), "Country"] = "Korea, Republic of"
df_data.loc[(df_data["Country"] == 'North Korea'), "Country"] = "Korea, Democratic People's Republic of"
df_data.loc[(df_data["Country"] == 'Kazakhstan'), "Country"] = "Russian Federation"

countries = {country.name: key for key, country in iso.countries_by_alpha3.items()}
df_data = df_data.replace({"Country": countries})

launches = df_data["Country"].value_counts().rename_axis("Country").reset_index(name='counts')
launches.head()

world_map = px.choropleth(launches, locations="Country", color="counts", color_continuous_scale=px.colors.sequential.matter)
world_map.update_layout(coloraxis_showscale=True)
world_map.show()
df_data.head()

# Show the number of failures by country
statuses = df_data.groupby("Country")["Mission_Status"].value_counts().rename_axis(["Country", "Status"]).reset_index(name='counts')
failures = statuses[statuses["Status"].str.contains("Fail")].groupby("Country").sum()

world_map = px.choropleth(failures, locations=failures.index, color="counts", color_continuous_scale=px.colors.sequential.matter)
world_map.update_layout(coloraxis_showscale=True) 
world_map.show()

# Create a Plotly Sunburst Chart of the countries, organisations, and mission status
sunburst = df_data.groupby(by=["Country", "Organisation", "Mission_Status"], as_index=False).size()
sunburst = sunburst.sort_values("size", ascending=False)
sunburst.head()
px.sunburst(sunburst, path=["Country", "Organisation", "Mission_Status"], values="size", title="Missions By Country")


# Analyse the total amount of money spent by organisation on space missions
money_spent = df_data[df_data["Price"].notna()]

money_spent["Price"] = money_spent["Price"].str.replace(',', '').astype(float)

total_money_spent = money_spent.groupby("Organisation")["Price"].sum().reset_index()
total_money_spent.sort_values(by="Price", ascending=False)
total_money_spent.head()

# Analyse the amount of money spent by organisation per launch
organisation_expense = money_spent.groupby("Organisation")["Price"].mean().reset_index()
organisation_expense.sort_values("Price", ascending=False)
organisation_expense.head()

# Converted the date to the datetime object, then extracted the year from the datetime object.
df_data['date'] = pd.to_datetime(df_data['Date'])
df_data['year'] = df_data['date'].apply(lambda datetime: datetime.year)
# df_data['year'].head()

# Counted the number of times the same year is mentioned.
ds = df_data['year'].value_counts().reset_index()
ds.columns = [
    'year', 
    'count'
]
# Passing the year and the count to the bar graph.
fig = px.bar(
    ds, 
    x='year', 
    y="count", 
    orientation='v', 
    title='Missions number by year' 
)
fig.show()

'''
Which month has seen the highest number of launches in all time? Superimpose a rolling average on the month on month time series chart.
'''

# Converted the date to the datetime object, then extracted the month from the datetime object.
df_data['date'] = pd.to_datetime(df_data['Date'])
df_data['month'] = df_data['date'].apply(lambda datetime: datetime.month)
# df_data['month'].head()

# Counted the number of times the same month is mentioned.
ds = df_data['month'].value_counts().reset_index()
ds.columns = [
    'month', 
    'count'
]
# Passing the year and the count to the bar graph.
fig = px.bar(
    ds, 
    x='month', 
    y="count", 
    orientation='v', 
    title='Missions number by month' 
)
fig.show()

# Using max to find the most launches per month
most_launches = ds['count'].max()
print("Most launches in a month =", most_launches)

# print the month associated with the max value
ds.sort_values(by="count", ascending=False)
ds.max()

#Using min to find the least launches per month
least_launches = ds['count'].min()
print("Least launches in a month =", least_launches)
ds.min()

# Create a line chart that shows the average price of rocket launches over time
avg_price = df_data[df_data["Price"].notna()]
pd.options.mode.chained_assignment = None
avg_price["Price"] = avg_price["Price"].str.replace(',', '').astype(float)

avg_price.groupby("year").mean().plot(figsize=(12, 8))

# Grab data from Organisations and Locations columns
# Sort through data to find the top 10 Organisations 
top_10=pd.DataFrame(columns=df_data.columns)
for val in df_data.groupby("Organisation").count().sort_values("Date",ascending=False)[:10].index:
  print(val)
  org=df_data[df_data.Organisation==val]
  top_10=top_10.append(org,ignore_index=False, verify_integrity=False, sort=None)

# Create a chart to display the data
px.histogram(top_10.sort_values(by=["Organisation", "Date"], ascending=[True, False]), x="Organisation",nbins=10) 


# Cold war space race: USA vs USSR
Or_df = df_data[(df_data['Country']=='USA') | (df_data['Country']=='RUS')]
# Sort years
cold_war_years = Or_df.sort_values("year")
# Grab years from start of dataset (1964) til 1991
cold_war_years[(cold_war_years.year <= 1991)]

# Comparing the total number of launches of the USSR and the USA
# Grab the data for USA and for Russian Federation (aka USSR)
Or_df = df_data[(df_data['Country']=='USA') | (df_data['Country']=='RUS')]

# Do not need to count the data - since the pie chart will collect the data per country. However, getting the count will help us to know if the data pulled into the pie chart is accurate.
launches = Or_df['Country'].value_counts().rename_axis('Country').reset_index(name='counts')
launches.head()

# Plot chart using Country and Mission_Status
colors = ["#1f77b4", "#ff7f0e"]
grouping = Or_df.groupby("Country").count().reset_index()
sizes = grouping['Mission_Status']
labels = grouping['Country']

plt.pie(sizes, labels = labels, colors = colors)

# Plot chart to show the total number of launches year-on-year
Or_df = df_data[(df_data['Country']=='USA') | (df_data['Country']=='RUS')]
Or_df.groupby(["year", "Country"]).size().unstack().plot()

# Chart the total number of mission failures year-on-year
Or_df = df_data[df_data['Mission_Status'].str.contains("Failure")]
yearly_failures = px.data.tips()
fig = px.sunburst(Or_df, path=["year", "Mission_Status"])
fig.show()

# Chart the percentage of failures over time
grouping = Or_df.groupby("year").count().reset_index()
sizes = grouping['Mission_Status']
labels = grouping['year']

plt.pie(sizes, labels = labels)
fig = plt.gcf()
fig.set_size_inches(15,15)
plt.show()

# Create a year-on-year chart showing the organisation doing the most number of launches
org_launches = df_data.groupby("year")["Organisation"].value_counts().rename_axis(["year", "Organisation"]).reset_index(name='counts')

# Group by year, then by country, then find max count
org_launches.loc[org_launches.groupby("year")["counts"].idxmax()]
org_launches.head()

org_set = set(org_launches['Organisation'])

plt.figure(figsize=(12, 10), dpi=80)
for org in org_set:
     selected_data = org_launches.loc[org_launches['Organisation'] == org]
     plt.plot(selected_data['year'], selected_data['counts'], label=org)
   
plt.legend()
plt.show()