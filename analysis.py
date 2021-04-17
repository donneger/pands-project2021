# An Investigation into Fishers Iris Data set utilising Python. 
# Progarmming and Scripting 2021
# Author: Gerard Donnelly

# Import the libraries needed for the program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#set up the variable to hold the dataset
irisdata = "irisdata.csv"

#Read in the data set and add the column names per the attribute information below:
irisdf = pd.read_csv(irisdata, names=["Sepal_Length", "Sepal_Width" , "Petal_Length", "Petal_Width", "Class"])
	#Attribute Information:
	#1. sepal length in cm
	#2. sepal width in cm
	#3. petal length in cm
	#4. petal width in cm
	#5. class:
	#-- Iris Setosa
	#-- Iris Versicolour
	#-- Iris Virginica

#This function creates the plots for the statistical analysis - Summary Plots


# Access to program functions from user menu function. 
def main():
	display_menu()
	while True:
		choice = input("Enter choice: ")
		if (choice == "1"):
			view_data()
			display_menu()
		elif (choice == "2"):
			view_stats()
			display_menu()
		elif (choice == "3"):
		
			display_menu()
		elif (choice == "4"):
			print("Thank you, program now exits.")
			break


# Function to display user menu.
def display_menu():
    print("\nFishers Iris Dataset, a Python Analysis")
    print("-"*39)
    print("User MENU")
    print("="*9)
    print("1 - View Dataset")
    print("2 - Run Statistics")
    print("3 - Generate Plots")
    print("4 - Exit Application")


#This function imports the raw Iris dataset, generates a number of summaries and saves results to csv files.   
#https://archive.ics.uci.edu/ml/datasets/iris
#https://pandas.pydata.org/docs/user_guide/index.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
def view_data():
    
#Summarise the data set and transpose for readibility
	datasummary = (irisdf.describe()).transpose()
	datahead = (irisdf.head(5))
	datatail = irisdf.tail(5)


# Output the Basic characteristics of the dataset to the screen. 	https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html
	print("\n1. This shows the data type of the set.\n", "\t",type(irisdf))
	print("\n2. This shows the shape of the data, i.e. number of rows and columns.\n","\t",irisdf.shape)
	print("\n3. Overall summary of the data\n", datasummary, "\n")
	print("\n4. First 5 lines of the dataset\n",irisdf.head(5), "\n")
	print("\n5. Last 5 lines of the dataset\n",irisdf.tail(5),"\n")


#Write the resulting summary tables to csv files. 
	datasummary.to_csv("datasummary.csv")
	datahead.to_csv("datahead.csv")
	datatail.to_csv("datatail.csv")	
	
	return


#This function performs a preliminary statistical analysis - Summary Statistics
def view_stats():
    	
#Set up the basic statistics of the dataset. 	
	classcount = irisdf.groupby("Class").count()
	classmean = irisdf.groupby("Class").mean()
	classmax = irisdf.groupby("Class").max()
	classmin = irisdf.groupby("Class").min()
	classmedian = irisdf.groupby("Class").median()
	classstd = irisdf.groupby("Class").std()

# Output the resulting details to csv files. 
	classcount.to_csv("classcount.csv")
	classmean.to_csv("classmean.csv")
	classmax.to_csv("classmax.csv")
	classmin.to_csv("classmin.csv")
	classmedian.to_csv("classmedian.csv")
	classstd.to_csv("classstd.csv")
	
	
# Print the details to the screen. 
	print("\n1. Dataset COUNT. This table shows the number of records per characteristic grouped by species in the dataset.\n",classcount)
	print("\n2. Dataset MEAN. This table shows the mean of the characteristics grouped by species in the dataset.\n",classmean)
	print("\n3. Dataset MAX. This table shows the max of the characteristics grouped by species in the dataset.\n",classmax)
	print("\n4. Dataset MIN. This table shows the min of the characteristics grouped by species in the dataset.\n",classmin)
	print("\n3. Dataset MED. This table shows the median of the characteristics grouped by species in the dataset.\n",classmedian)
	print("\n3. Dataset STD.DEV. This table shows the standard deviation of the characteristics grouped by species in the dataset.\n",classstd)
	return

if __name__ == "__main__":
		main()

#sns.pairplot(irisdf, hue='Class', height=2.0).fig.suptitle("Iris Data Scatter Plots", fontsize=20)
#irisdf.plot()
#plt.show(block=True)

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

