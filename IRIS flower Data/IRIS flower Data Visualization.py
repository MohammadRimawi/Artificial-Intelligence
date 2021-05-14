import pandas as pd
import matplotlib as plt
import plotly.express as px
#%%

IRIS_DATA = pd.read_csv("IRIS.csv")
cp = pd.DataFrame(IRIS_DATA)
cp = cp.fillna(0)
print(cp)


#%%

# Bar chart on sepal_length
grs = cp.groupby(["species"])[["sepal_length"]].mean().reset_index()
fig = px.bar(grs[['species', 'sepal_length']].sort_values('sepal_length', ascending=False), 
             y="sepal_length", x="species", color='species', 
             log_y=True, template='ggplot2',title="Bar chart on sepal_length")
fig.show()

#%%


#%%
# Bar chart on sepal_width

grs = cp.groupby(["species"])[["sepal_width"]].mean().reset_index()
fig = px.bar(grs[['species', 'sepal_width']].sort_values('sepal_width', ascending=False), 
             y="sepal_width", x="species", color='species', 
             log_y=True, template='ggplot2',title="Bar chart on sepal_width")
fig.show()

#%%
# Bar chart on petal_length

grs = cp.groupby(["species"])[["petal_length"]].mean().reset_index()
fig = px.bar(grs[['species', 'petal_length']].sort_values('petal_length', ascending=False), 
             y="petal_length", x="species", color='species', 
             log_y=True, template='ggplot2',title="Bar chart on petal_length")
fig.show()

#%%

#%%
# Bar chart on petal_width

grs = cp.groupby(["species"])[["petal_width"]].mean().reset_index()
fig = px.bar(grs[['species', 'petal_width']].sort_values('petal_width', ascending=False), 
             y="petal_width", x="species", color='species', 
             log_y=True, template='ggplot2',title="Bar chart on petal_width")
fig.show()

#%%

