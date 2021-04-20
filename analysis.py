# An Investigation into Fishers Iris Data set utilising Python. 
# Progarmming and Scripting 2021
# Author: Gerard Donnelly

# Import the libraries needed for the program.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#set up the variable to hold the dataset that is stored as irisdata,csv.
irisdata = (r'tables/irisdata.csv')

#Read in the data set and add the column names per the attribute information below:
irisdf = pd.read_csv(irisdata, names=['Sepal_Length', 'Sepal_Width' , 'Petal_Length', 'Petal_Width', 'Class'])
#Attribute Information in the dataset:
	#1. sepal length in cm
	#2. sepal width in cm
	#3. petal length in cm
	#4. petal width in cm
	#5. class:
	#-- Iris Setosa
	#-- Iris Versicolour
	#-- Iris Virginica

#https://archive.ics.uci.edu/ml/datasets/iris
#https://pandas.pydata.org/docs/user_guide/index.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

#Summarise the data set and transpose for readibility
datasummary = (irisdf.describe()).transpose().round(4)
datahead = (irisdf.head(5))
datatail = irisdf.tail(5)

# Output the Basic characteristics of the dataset to the screen. 	https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html
print('\n1. This shows the data type of the set.\n', '\t',type(irisdf))
print('\n2. This shows the shape of the data, i.e. number of rows and columns.\n','\t',irisdf.shape)
print('\n3. Overall summary of the data\n', datasummary, '\n')
print('\n4. First 5 lines of the dataset\n',irisdf.head(5), '\n')
print('\n5. Last 5 lines of the dataset\n',irisdf.tail(5),'\n')

#Write the resulting summary tables to csv files. 
datasummary.to_csv(r'tables/datasummary.csv')
datahead.to_csv(r'tables/datahead.csv')
datatail.to_csv(r'tables/datatail.csv')	

# Set up the variables to hold the basic statistical characteristicsa of the dataset, grouped by Iris species. 
classcount = irisdf.groupby('Class').count()
classmean = irisdf.groupby('Class').mean().round(4)
classmax = irisdf.groupby('Class').max().round(4)
classmin = irisdf.groupby('Class').min().round(4)
classmedian = irisdf.groupby('Class').median().round(4)
classstd = irisdf.groupby('Class').std().round(4)
classcor= irisdf.corr().round(4)

# Output the resulting details to csv files. 
classcount.to_csv(r'tables/classcount.csv')
classmean.to_csv(r'tables/classmean.csv')
classmax.to_csv(r'tables/classmax.csv')
classmin.to_csv(r'tables/classmin.csv')
classmedian.to_csv(r'tables/classmedian.csv')
classstd.to_csv(r'tables/classstd.csv')
classcor.to_csv(r'tables/classcorr.csv')

# Print the details to the screen. 
print('\n1. Dataset COUNT. This table shows the number of records per characteristic grouped by species in the dataset.\n',classcount)
print('\n2. Dataset MEAN. This table shows the mean of the characteristics grouped by species in the dataset.\n',classmean)
print('\n3. Dataset MAX. This table shows the max of the characteristics grouped by species in the dataset.\n',classmax)
print('\n4. Dataset MIN. This table shows the min of the characteristics grouped by species in the dataset.\n',classmin)
print('\n3. Dataset MED. This table shows the median of the characteristics grouped by species in the dataset.\n',classmedian)
print('\n3. Dataset MED. This table shows the standard deviation of the characteristics grouped by species in the dataset.\n',classstd)
print('\n3. Dataset Coorelation. This table shows the pairwuse correlation of the characteristics grouped by species in the dataset.\n',classcor)


# All of the code below generate and outputs the plots from the data.
# This code generates a full pair plot comparing all of the characteristics against each other across the 3 species. 
#https://seaborn.pydata.org/tutorial/axis_grids.html
sns.pairplot(irisdf, hue='Class', height=2.0)
plt.savefig(r'plots/irispairplot.png')


plt.clf()

# Overall Petal Length vs Petal Width
sns.histplot(irisdf["Petal_Length"], color="green", label="Petal_Length")
sns.histplot(irisdf["Petal_Width"], color="blue", label= "Petal_width")
plt.xlabel("")
plt.legend()
plt.savefig(r'plots/histcompare_petalL_petalW.png')


plt.cla()

#Overall Sepal Length vs Sepal Width
sns.histplot(irisdf["Sepal_Length"], color="green", label="Sepal_Length")
sns.histplot(irisdf["Sepal_Width"], color="blue", label= "Sepal_width")
plt.xlabel("")
plt.legend()
plt.savefig(r'plots/histcompare_sepalL_sepalW.png')


plt.clf()


# Comparing Sepal Length across the species. 
g=sns.FacetGrid(irisdf, col="Class", hue="Class")
g.map(sns.histplot, "Sepal_Length")
plt.savefig(r'plots/histsepalLen_species.png')

plt.clf()
# Comparing Sepal Width across the species. 
g=sns.FacetGrid(irisdf, col="Class", hue="Class")
g.map(sns.histplot, "Sepal_Width")
plt.savefig(r'plots/histsepalWid_species.png')

plt.clf()
# Comparing Petal Length across the species. 
g=sns.FacetGrid(irisdf, col="Class", hue="Class")
g.map(sns.histplot, "Petal_Length")
plt.savefig(r'plots/histpetalLen_species.png')

plt.clf()
# Comparing Petal Width across the species. 
g=sns.FacetGrid(irisdf, col="Class", hue="Class")
g.map(sns.histplot, "Petal_Width")
plt.savefig(r'plots/histpetalWid_species.png')

plt.clf()

#Complete set of Boxplats across the species. https://dev.to/thalesbruno/subplotting-with-matplotlib-and-seaborn-5ei8
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Boxplots of Characteristics across the Species")
sns.boxplot(ax=axes[0, 0], data=irisdf, x='Class', y='Sepal_Length')
sns.boxplot(ax=axes[0, 1], data=irisdf, x='Class', y='Sepal_Width')
sns.boxplot(ax=axes[1, 0], data=irisdf, x='Class', y='Petal_Length')
sns.boxplot(ax=axes[1, 1], data=irisdf, x='Class', y='Petal_Width')
plt.savefig(r'plots/boxplots_species.png')

#Regression Testing Plots: https://seaborn.pydata.org/generated/seaborn.lmplot.html
# Regression Petal L vs W
sns.lmplot(x="Petal_Length", y="Petal_Width", col="Class", hue="Class", data=irisdf)
plt.savefig(r'plots/regression_Petal_length_width.png')

# Regression Sepal L vs W
sns.lmplot(x="Sepal_Length", y="Sepal_Width", col="Class", hue="Class", data=irisdf)
plt.savefig(r'plots/regression_Sepal_length_width.png')

# Regression Petal L vs Sepal L
sns.lmplot(x="Petal_Length", y="Sepal_Length", col="Class", hue="Class", data=irisdf)
plt.savefig(r'plots/regression_length_Petal_Sepal.png')

# Regression Petal W vs Sepal W
sns.lmplot(x="Petal_Width", y="Sepal_Width", col="Class", hue="Class", data=irisdf)
plt.savefig(r'plots/regression_width_Petal_Sepal.png')

print("The program has completed successfully. All of the tables have been stored in the Tables folder and the plots in the Plots folder. Thank you.")
