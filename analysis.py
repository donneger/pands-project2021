# An Investigation into Fishers Iris Data set utilising Python. 
# Progarmming and Scripting 2021
# Author: Gerard Donnelly

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "irisdata.csv"

df = pd.read_csv(filename, names=["Sepal_Length", "Sepal_Width" , "Petal_Length", "Petal_Width", "Class"])

print(df.describe())

print(df.head(5))

print(df.tail(5))

print(df.groupby(pd.Grouper(key="Class")).mean())

#df.plot()
#df.plot.hist(stacked=True)
#df.diff().hist(color="k", alpha=0.5, bins=50)
df.plot.box()
#df.plot.area()
#ax = df.plot.scatter(x="Petal_Length", y = "Class", color="DarkBlue", label = "PL")
#df.plot.scatter(x="Sepal_Width", y = "Class", color="DarkGreen", label = "PW", ax = ax)
#from pandas.plotting import scatter_matrix
#scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal="kde")

plt.show()