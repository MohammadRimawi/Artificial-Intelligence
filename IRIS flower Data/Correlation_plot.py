import pandas as pd
# import matplotlib as plt
import matplotlib.pyplot as plt
import plotly.express as px
#%%

IRIS_DATA = pd.read_csv("IRIS.csv")
cp = pd.DataFrame(IRIS_DATA)
cp = cp.fillna(0)

print(cp)

#%%

cor = cp.loc[:,["petal_length","petal_width","sepal_length","sepal_width","species"]]
fig = plt.figure(figsize = (10, 5))
ax = fig.add_subplot()
ax.imshow(cor.corr())
#%%