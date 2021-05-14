import pandas as pd
import seaborn as sns
#%%

IRIS_DATA = pd.read_csv("IRIS flower Data/IRIS.csv")
cp = pd.DataFrame(IRIS_DATA)
cp = cp.fillna(0)
print(cp)


#%%


sns.set(style="darkgrid")
ax = sns.countplot(x="species", data=cp)


#%%