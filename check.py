# An Investigation into Fishers Iris Data set utilising Python. 
# Progarmming and Scripting 2021
# Author: Gerard Donnelly

# Import the libraries needed for the program.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def display():
    irisdata = (r'tables/irisdata.csv')
    irisdf = pd.read_csv(irisdata, names=["Sepal_Length", "Sepal_Width" , "Petal_Length", "Petal_Width", "Class"])
    print(irisdf.head(5))
    irisdf.plot()
    plt.show()
    return

enter = input("input a number:")
if (enter == "1"):
    display()