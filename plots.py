import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
sns.set()

#set up the variable to hold the dataset
def printplot():
    print("got here")
    irisdata = "irisdata.csv"

    #Read in the data set and add the column names per the attribute information below:
    irisdf = pd.read_csv(irisdata, names=["Sepal_Length", "Sepal_Width" , "Petal_Length", "Petal_Width", "Class"])

    plt.boxplot(x="Petal_Length", y="Sepal_Length", data=irisdf)
    plt.show()
    return

printplot()