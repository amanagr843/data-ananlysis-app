import pandas as pd

data = pd.read_csv("data/test_merged_10.csv", engine='python')
# data["State Name"] = data["State Name"].sort_values(ascending=True).values
# data["District Name"] = data["District Name"].sort_values(ascending=True).values
# data["Sub District Name"] = data["Sub District Name"].sort_values(ascending=True).values
data.dropna(subset = ["State Name"], inplace=True)
data.dropna(subset = ["District Name"], inplace=True)
data.dropna(subset = ["Sub District Name"], inplace=True)
data.sort_values("Total Population of Village",axis=0,ascending = False,inplace = True)
