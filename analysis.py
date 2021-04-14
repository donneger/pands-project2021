# An Investigation into Fishers Iris Data set utilising Python. 
# Progarmming and Scripting 2021
# Author: Gerard Donnelly

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Setting up to import the raw Iris data set. https://archive.ics.uci.edu/ml/datasets/iris
irisdata = "irisdata.csv"

#Read in the data set and add the column names per the attribute information below:
#Attribute Information:
    #1. sepal length in cm
    #2. sepal width in cm
    #3. petal length in cm
    #4. petal width in cm
    #5. class:
    #-- Iris Setosa
    #-- Iris Versicolour
    #-- Iris Virginica
irisdf = pd.read_csv(irisdata, names=["Sepal_Length", "Sepal_Width" , "Petal_Length", "Petal_Width", "Class"])

#Summarise the data set and transpose for readibility
datasummary = (irisdf.describe()).transpose()

datasummary.to_csv("summarytest.csv")

print(datasummary, "\n")
print(irisdf.head(5), "\n")
print(irisdf.tail(5),"\n")

#cols = irisdf.loc[irisdf["Sepal_Length"] > mean(),"Class"]

#print(cols)
#print(irisdf.shape)
#print(type(irisdf))

#First Analysis - Summary Statistics
print(irisdf.groupby("Class").count())
print(irisdf.groupby("Class").mean())
print(irisdf.groupby("Class").max())
print(irisdf.groupby("Class").min())
print(irisdf.groupby("Class").median())
print(irisdf.groupby("Class").std())

#print(irisdf.groupby(pd.Grouper(key="Class")).mean())



#irisdf.plot()
#irisdf.plot.hist(stacked=True)
#irisdf.diff().hist(color="k", alpha=0.5, bins=50)
#df1 = irisdf.boxplot(by="Class", grid=False, rot=45, fontsize=15)
#irisdf.plot.area()
#ax = irisdf.plot.scatter(x="Petal_Length", y = "Class", color="DarkBlue", label = "PL")
#irisdf.plot.scatter(x="Sepal_Width", y = "Class", color="DarkGreen", label = "PW", ax = ax)
#from pandas.plotting import scatter_matrix
#scatter_matrix(irisdf, alpha=0.2, figsize=(6, 6), diagonal="kde")

#plt.show()


''' plt.figure(facecolor = 'lightcyan') 

# This section creates and formats the individual plot lines. # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html.
# It is a tiny subset of the vast number of options availabel for plotting. 
# First is the line style and color, MS is line marker size, mec and mfc set the markers face and edge colors, label applies a legend to the plot . 
plt.plot(x, x, 'o-r', ms=10, mec = 'b', mfc = 'r', label = 'Linear f(x)')
plt.plot(x, x**2, 'o--g', ms=10, mec = 'r', mfc = 'b', label = 'Quadratic g(x^2)')
plt.plot(x, x**3, 'o-.b', ms=10, mec = 'b', mfc = 'g', label = 'Cubed (h^2)')

#This section formats the plot axes, titles, gridlines, fontsize and displays the resulting plot using various options to test out different formatting. 
ax = plt.axes()
ax.set_facecolor('bisque')
plt.xticks(x)
plt.legend(fontsize = 15)
plt.title('Week 8 Lab Plotting', fontsize = 20, fontweight = 'bold', style = 'italic')
plt.xlabel('Dimension (x)', fontsize = 15)
plt.ylabel('Function(y)', fontsize = 15)
plt.grid(linestyle = 'dashed')
plt.show() '''