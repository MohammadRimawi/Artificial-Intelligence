import pandas as pd
# import matplotlib as plt
import matplotlib.pyplot as plt
import plotly.express as px
#%%

IRIS_DATA = pd.read_csv("IRIS.csv")
cp = pd.DataFrame(IRIS_DATA)
cp = cp.fillna(0)
cp["count"] = cp.groupby(['species'])['species'].transform('count')
print(cp)


#%%
plt.title("scatter plot on sepal_length against petal_length")
plt.scatter(cp["sepal_length"],cp["petal_length"])
plt.show()
#%%

#%%
plt.title("scatter plot on sepal_width against petal_width")
plt.scatter(cp["sepal_width"],cp["petal_width"])
plt.show()
#%%