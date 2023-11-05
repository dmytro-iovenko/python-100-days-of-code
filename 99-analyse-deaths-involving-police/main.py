import pandas as pd

data = pd.read_csv("deaths_by_police.csv")

print(data.shape)
data.head()