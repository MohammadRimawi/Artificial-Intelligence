
import pandas as pd
import SimpSOM as sps
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder

#%%

IRIS_DATA = pd.read_csv("IRIS.csv")
cp = pd.DataFrame(IRIS_DATA)
cp = cp.fillna(0)
cp["species"]= OrdinalEncoder().fit_transform(cp[["species"]])
print(cp)


#%%

cp = cp.sample(n=50, random_state=0)
cpSt = StandardScaler().fit_transform(cp.values)
net = sps.somNet(30, 30, cpSt, PBC=True, PCI=True)
net.train(0.1, 10000)
net.diff_graph(show=True,printout=True)

#%%