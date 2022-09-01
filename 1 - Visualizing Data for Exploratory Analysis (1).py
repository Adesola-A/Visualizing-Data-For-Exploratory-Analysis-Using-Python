#!/usr/bin/env python
# coding: utf-8

# # Visualizing Data for Exploratory Analysis
# In this chapter we will explore two more Python packages: Matplotlib and Seaborn. Both of them are data visualization tools in Python that helps us create informative charts and graphs. 
# 
# To start, we'll import all of the packages that we'll use in this chapter. Import numpy as np and pandas as pd. Then, we'll import a module inside the `matplotlib` package called `pyplot`, and alias it as `plt`. We'll also import `seaborn` as `sns`. 
# 
# After importing the packages, we need to add one more line of code: %matplotlib inline. With this line of code, the plot output will be displayed in Jupyter Notebook directly below the code cell that produces it. The plots will also be stored in the notebook document.

# In[1]:


# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# We will continue to work with financial data throughout this chapter, using the Pandas DataReader package once again to connect to data from Yahoo Finance. 
# 
# We will start by creating three separate DataFrames that contain information for stocks and bonds. We are going to import one column for each DataFrame, the adjusted close of the stock or bond for each day.

# In[3]:


import pandas_datareader.data as pdr

# Setting dates for the DataFrames
startdate = '2021-01-01'
enddate = '2022-12-31'

# Using 'SPY ETF' as a proxy for general market
stocks = pdr.DataReader('SPY','yahoo', startdate, enddate)[['Adj Close']]

# Using '20 year ETF' as a proxy for bonds
bonds = pdr.DataReader('TLT','yahoo', startdate, enddate)[['Adj Close']]

# Using 'USO ETF' as a proxy for the price of oil
oil = pdr.DataReader('USO','yahoo', startdate, enddate)[['Adj Close']]

print(stocks.head())
print(bonds.head())
print(oil.head())


# In[4]:


stocks.info()


# Currently, the `Adj Close` column is the value of the stock for each day. For this example, let's change the adjusted close to a percent change from the previous day. We can make this change by using the `pct_change()` function from pandas.

# In[5]:


# Converting Adj Close to percent returns
stocks = stocks.pct_change()
bonds = bonds.pct_change()
oil = oil.pct_change()

print(stocks.head())
print(bonds.head())
print(oil.head())


# Let's create one more DataFrame by concatenanting `stocks`, `bonds`, and `oil` into `stocksandBonds`. This DataFrame will have the date as the index and three columns: the percent change of the adjusted close for the stocks.

# In[6]:


# Using prior example and concating returns column wise and keeping matching dates

StocksAndBonds = pd.concat([stocks, bonds, oil], axis=1, join = 'inner')
# Renaming columns
StocksAndBonds.columns = ['SPY', 'TLT', 'USO']
StocksAndBonds.head()


# Now we have `bonds`, `stocks`, `oil`, and `stocksandBonds` available for us to visualize.

# # Creating Histograms
# In this lesson we'll create some histograms, also know as distribution plots. This type of graph visualizes how often a certain value occurs in our dataset. The frequency of each value is plotted, so we can see the distrubution of the values.

# In[11]:


# Create a histogram, or distribution plot, for stocks
sns.histplot(StocksAndBonds['SPY'])


# One of the main arguments we can use the control the display of our histograms is `bins`. This defines the number of columns that we want to appear in our histogram. This can help us dig into the distribution of our data in more detail, or provide a more high-level view.

# In[12]:


# Set the number of bins, or columns, to appear in the plot
sns.histplot(StocksAndBonds['SPY'], bins= 50)


# We can also view multiple columns from our data set in a single histogram. To display all three of our stocks, we can input the name of our DataFrame without specifying any columns. We can control how we want to the distribution of the different columns to display. To do this, we use the `multiple` argument, to define if the columns should overlap each other, or go side by side.

# In[13]:


# Create a histogram for all columns in the DataFrame
sns.histplot(StocksAndBonds, bins = 25, multiple = 'dodge')


# In[ ]:


# Create a histogram for stocks and bonds, using multiple column names in a list


# # Creating Box Plots
# A box plot, or a box and whisker plot, is used to visualize the distribution of data. This visual uses some summary statistics in order to compare the distribution of different categories, or columns, in a data set:
# * Minimum
# * Q1 - first quartile
# * Q2 - Median
# * Q3 - third quartile
# * Maximum
# 
# These five points are located at each end of the whiskers, each end of the box, and the line in the middle of the box. Outliers are shown as points that occur outside of the minimum and maximum values.

# In[14]:


# Visual summary statistics of each category
sns.histplot(StocksAndBonds[['SPY', 'TLT']], bins = 25, multiple='layer')


# In[ ]:


# Select two categories to compare


# # Creating a Pairplot
# A pairplot allows us to view multiple scatter and distribution plots in a single visual. This way, we can see multiple relationships, between different variables, in one view.

# In[15]:


sns.pairplot(StocksAndBonds)


# In the diagonal line, we see a distribution plot of a single column. In the other sections, we have a scatter plot that shows the relationship between two different variables. We'll cover scatter plots in more detail later in the course.

# # Creating a Correlation Matrix Heatmap
# As we saw in the previous chapter, correlation is a method to evaluate the strength of a relationship between two continous variables. Correlation shows not only the direction between two variables, but also the magnitude of the relationship. `Correlation` values are between -1 and 1, with -1 being a perfect negative correlation, and 1 being a perfect positive correlation. A value of 0 indicates that there is no relationship between the two variables.

# In[ ]:


# Correlation matrix for the three stocks


# In[ ]:


# Visualize the correlation matrix


# Three common arguments to control the display of a heatmap are:
# * vmin & vmax
# * annot
# * cmap
# 
# `vmin` and `vmax` control the scale of the heatmap. As correlation is measured between -1 and 1, we can update the minimum value to -1.
# 
# The `annot` argument allows us to display the values of a section in the heatmap. We can set this to `True` to see the correlation coefficient for each section.
# 
# The `cmap` argument lets us set the color of the scale in the heatmap. There are several built-in options to choose from. We can update our heatmap to use the `coolwarm` option.

# In[ ]:


# Update the correlation matrix

