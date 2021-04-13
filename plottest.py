# Program to display the plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on a single set of axes.
# Author: Gerry Donnelly.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4]) # Set up the function range. 

# This section sets up the plots for each of the functions'
# Colors sourced from https://matplotlib.org/stable/gallery/color/named_colors.html
# Sets the facecolor of the plot, i.e. the color surrounding the plot. 
plt.figure(facecolor = 'lightcyan') 

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
plt.show()