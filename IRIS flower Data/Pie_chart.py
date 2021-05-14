import pandas as pd
import matplotlib as plt
import plotly.express as px
#%%

IRIS_DATA = pd.read_csv("IRIS.csv")
cp = pd.DataFrame(IRIS_DATA)
cp = cp.fillna(0)
cp["count"] = cp.groupby(['species'])['species'].transform('count')
print(cp)


#%%
grdsp = cp.groupby(["species"])[["count"]].mean().reset_index()

fig = px.pie(grdsp,
             values="count",
             names="species",
             template="seaborn",title="Pie chart on count")
fig.update_traces(rotation=90, pull=0.05, textinfo="percent+label")
fig.show()
#%%