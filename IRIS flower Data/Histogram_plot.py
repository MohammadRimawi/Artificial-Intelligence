import pandas as pd
import matplotlib as plt
import plotly.express as px
#%%

IRIS_DATA = pd.read_csv("IRIS.csv")
cp = pd.DataFrame(IRIS_DATA)
cp = cp.fillna(0)
print(cp)


#%%
# Histogram based on sepal_length

fig = px.histogram(cp, x="sepal_length", color="species",log_y=True, template='ggplot2',title="Histogram chart on sepal_length")
fig.show()

#%%
# Histogram based on sepal_length

fig = px.histogram(cp, x="sepal_width", color="species",log_y=True, template='ggplot2',title="Histogram chart on sepal_width")
fig.show()

#%%
# Histogram based on sepal_length

fig = px.histogram(cp, x="petal_length", color="species",log_y=True, template='ggplot2',title="Histogram chart on petal_length")
fig.show()

#%%
# Histogram based on sepal_length

fig = px.histogram(cp, x="petal_width", color="species",log_y=True, template='ggplot2',title="Histogram chart on petal_width")
fig.show()

#%%