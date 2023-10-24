import pandas as pd
import plotly.express as px
import iso3166 as iso

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