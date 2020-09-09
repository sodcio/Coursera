
# coding: utf-8

# ## How to select dataframe subsets from multivariate data

# In[ ]:


import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe


# In[ ]:


# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")


# In[ ]:


df.head()


# ### Keep only body measures columns, so only columns with "BMX" in the name

# In[ ]:


# get columns names
col_names = df.columns
col_names


# In[ ]:


# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
       'BMXWAIST']


# In[ ]:


# Another way to get only column names that include 'BMX' is with list comprehension
# [keep x for x in list if condition met]
[column for column in col_names if 'BMX' in column]


# In[ ]:


keep = [column for column in col_names if 'BMX' in column]


# In[ ]:


# use [] notation to keep columns
df_BMX = df[keep]


# In[ ]:


df_BMX.head()


# There are two methods for selecting by row and column. 
# # link for pandas cheat sheets
# * df.loc[row labels or bool, col labels or bool]
# * df.iloc[row int or bool, col int or bool]

# ### [From pandas docs](https://pandas.pydata.org/pandas-docs/stable/indexing.html]):  
# * [ ] column indexing
# * .loc is primarily label based, but may also be used with a boolean array.   
# * .iloc is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.

# In[ ]:


df.loc[:, keep].head()


# In[ ]:


index_bool = np.isin(df.columns, keep)


# In[ ]:


index_bool 


# In[ ]:


df.iloc[:,index_bool].head() # Indexing with boolean list


# ### Selection by conditions

# In[ ]:


# Lets only look at rows who 'BMXWAIST' is larger than the median
waist_median = pd.Series.median(df_BMX['BMXWAIST']) # get the median of 'BMXWAIST'


# In[ ]:


waist_median


# In[ ]:


df_BMX[df_BMX['BMXWAIST'] > waist_median].head()


# In[ ]:


# Lets add another condition, that 'BMXLEG' must be less than 32
condition1 = df_BMX['BMXWAIST'] > waist_median
condition2 = df_BMX['BMXLEG'] < 32
df_BMX[condition1 & condition2].head() # Using [] method
# Note: can't use 'and' instead of '&'


# In[ ]:


df_BMX.loc[condition1 & condition2, :].head() # Using df.loc[] method
# note that the conditiona are describing the rows to keep


# In[ ]:


# Lets make a small dataframe and give it a new index so can more clearly see the differences between .loc and .iloc
tmp = df_BMX.loc[condition1 & condition2, :].head()
tmp.index = ['a', 'b', 'c', 'd', 'e'] # If you use different years than 2015-2016, this my give an error. Why?
tmp


# In[ ]:


tmp.loc[['a', 'b'],'BMXLEG']


# In[ ]:


tmp.iloc[[0, 1],3]


# ### Common errors and how to read them

# In[ ]:


tmp[:, 'BMXBMI'] 


# ### Problem
# The above gives: TypeError: unhashable type: 'slice' 
# 
# The [ ] method uses hashes to identify the columns to keep, and each column has an associated hash. A 'slice' (a subset of rows and columns) does not have an associated hash, thus causing this TypeError.

# In[ ]:


tmp.loc[:, 'BMXBMI']


# In[ ]:


tmp.loc[:, 'BMXBMI'].values


# In[ ]:


tmp.iloc[:, 'BMXBMI']


# ### Problem
# The above gives: ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types
# 
# 'BMXBMI' is not an integer that is less than or equal number of columns -1, or a list of boolean values, so it is the wrong value type. 

# In[ ]:


tmp.iloc[:, 2]


# In[ ]:


tmp.loc[:, 2]


# ### Problem
# The above code gives: ```TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [2] of <class 'int'>```
# 
# 2 is not one of the labels (i.e. column names) in the dataframe

# In[ ]:


# Here is another example of using a boolean list for indexing columns
tmp.loc[:, [False, False, True] +[False]*4]


# In[ ]:


tmp.iloc[:, 2]


# In[ ]:


# We can use the .loc and .iloc methods to change values within the dataframe
tmp.iloc[0:3,2] = [0]*3
tmp.iloc[:,2]


# In[ ]:


tmp.loc['a':'c','BMXBMI'] = [1]*3
tmp.loc[:,'BMXBMI']


# In[ ]:


# We can use the [] method when changing all the values of a column
tmp['BMXBMI'] = range(0, 5)
tmp


# In[ ]:


# We will get a warning when using the [] method with conditions to set new values in our dataframe
tmp[tmp.BMXBMI > 2]['BMXBMI'] = [10]*2 # Setting new values to a copy of tmp, but not tmp itself
tmp
# You can see that the above code did not change our dataframe 'tmp'. This


# In[ ]:


# The correct way to do the above is with .loc or .iloc
tmp.loc[tmp.BMXBMI > 2, 'BMXBMI']  = [10]*2
tmp # Now contains the chances

