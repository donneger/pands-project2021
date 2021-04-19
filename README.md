						An Investigation into Fishers Iris Data set utilising Python.  

							GMIT - Programming and Scripting 2021 

								  Author: Gerard Donnelly
								         April 2021

 

# Introduction 
This project is in fulfillment of the course requirements for GMIT Programming and Scripting 2021, a module of the HDip in Data Analytics.  

# Project Objectives
1. Provide an overview of the Fishers Iris Dataset in the context of its significance to statistical analysis, particularly for statistical classification and machine learning. 
2. Using Python and associated libraries write a program to generate a complete analysis of the data set in both tabular and graphical forms.  
3. Based on the results of the analysis make observations of the significance of the results. 
4. Outpput the results to a project analysis document and make all project related documents available on my GitHub repository.

# Background and Description of the Dataset
The Iris flower dataset is also known as the Fisher’s Iris dataset. As a Fellow of the Royal Society, Sir Ronald Aylmer Fisher was born in 1890 in London, England, and was well-known as a statistician and geneticist. 
In 1936, Fisher published a report titled “The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics. In this article, Fisher developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers. It was the first time that the sepal and petal measures of the three Iris species, pictured below, appeared publicly.  

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Sepals typically act as protection or support for the flower. Petals are often brightly colored and provide clues as to a plant's classification. These measures, 150 in total across the three species, were used to create a linear model to classify the species. The dataset is often used in data mining, classification, and clustering examples and to test algorithms and is perhaps the best-known database to be found in the pattern recognition literature.3 

It is very clear that there is a significant body of information readily available across the internet relating to this dataset and associated analyses. The goal with this project is to carry out an analysis using generally accepted statistical and plotting techniques and analyses using Python and to validate the findings against the already existing results.   

There are several areas that will be outside the scope of this project, including deep statistical analysis and machine learning as I would have insufficient depth of knowledge in these subject areas to make well informed observations.  

# Project Approach
## General research on the subject.  
As described in the preceding paragraphs there are many sources of information available covering all aspects of analysis of the dataset.  

The dataset itself is widely available, in this case I have used the dataset from https://archive.ics.uci.edu/ml/datasets/iris. This dataset consists of 5 columns and 150 rows across the 3 iris species in a csv format.  

1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
- Iris Setosa 
- Iris Versicolour 
- Iris Virginica 

## Python 
This project utilises 4 Python libraries, namely: 

- Pandas. This is a powerful and flexible Python package that allows you to work with labeled and time series data. It also provides statistics methods, enables plotting, and more. One crucial feature of Pandas is its ability to write and read Excel, CSV, and many other types of files. 

- Numpy. This is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more. 

- Matplotlib. This is a powerful library that allows for creation of many types of plots and used in conjunction with Pandas allows for data series or dataframes to be plotted in many ways.  

- Seaborn. This is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. 

#Statistical Analysis 

The following are used in the Python program to provide a numerical overview of the data set and are assigned the following variables.  

In each case the analysis is grouped by Iris class and by characteristic across the 4 measurements.  

**Count**
classcount = irisdf.groupby('Class').count() 
The dataset consists of 50 measurements across the 3 species for each of the Petal Length and Width and Sepal Length and width.  
The output of this can be found in the table classcount.csv and confirms that the correct number of records are included in the dataset. 

**Mean**
classmean = irisdf.groupby('Class').mean() 
This is the mathematical average of the measurements and can be found in the table 		classmean.csv.  
On initial inspection it is clear that setosa petal length and width are significantly less than that 	of the other 2 species.  

**Max**
classmax = irisdf.groupby('Class').max() 
This is the maximum measurement for each of the measurement sets and can be found in the 	table classmax.csv.  
For Setosa the maximum measurement of petal length and width are significantly less than that 	of the other 2 species.  

**Min**
classmin = irisdf.groupby('Class').min() 
This is the minimum measurement for each of the measurement sets and can be found in the 	table classmin.csv.  
Like the analysis above the minimum measurement for setosa across petal length and width 	are significantly less that of the other 2 species.  

**Median**
classmedian = irisdf.groupby('Class').median() 
The measures the value at which 50% of the records are above and 50% below this value. The 	details can be found in the classmedian.csv table. 	 

**Standard Deviation**
classstd = irisdf.groupby('Class').std() 
The standard deviation is a measure of the amount of variation or dispersion of a set of values. A low standard deviation indicates that the values tend to be close to the mean (also called the expected value) of the set, while a high standard deviation indicates that the values are spread out over a wider range. 9 

**Correlation**
classcor= irisdf.corr() 
Correlation measures the extent to which there is a correlation, causal or not, between 2 	variables.  


# Graphical Analysis
This program produces a number of plots to provide a more comprehensive visual overview of the data. 

./plots/boxplots_species



