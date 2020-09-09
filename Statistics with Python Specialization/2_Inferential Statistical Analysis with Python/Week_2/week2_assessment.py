
# coding: utf-8

# ## Creating confidence intervals in python
# In this assessment, you will look at data from a study on toddler sleep habits. 
# 
# The confidence intervals you create and the questions you answer in this Jupyter notebook will be used to answer questions in the following graded assignment.

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import t
from scipy.stats import sem
import statistics 

pd.set_option('display.max_columns', 30) # set so can see all columns of the DataFrame


# Your goal is to analyse data which is the result of a study that examined
# differences in a number of sleep variables between napping and non-napping toddlers. Some of these
# sleep variables included: Bedtime (lights-off time in decimalized time), Night Sleep Onset Time (in
# decimalized time), Wake Time (sleep end time in decimalized time), Night Sleep Duration (interval
# between sleep onset and sleep end in minutes), and Total 24-Hour Sleep Duration (in minutes). Note:
# [Decimalized time](https://en.wikipedia.org/wiki/Decimal_time) is the representation of the time of day using units which are decimally related.   
# 
# 
# The 20 study participants were healthy, normally developing toddlers with no sleep or behavioral
# problems. These children were categorized as napping or non-napping based upon parental report of
# children’s habitual sleep patterns. Researchers then verified napping status with data from actigraphy (a
# non-invasive method of monitoring human rest/activity cycles by wearing of a sensor on the wrist) and
# sleep diaries during the 5 days before the study assessments were made.
# 
# 
# You are specifically interested in the results for the Bedtime, Night Sleep Duration, and Total 24-
# Hour Sleep Duration. 

# Reference: Akacem LD, Simpkin CT, Carskadon MA, Wright KP Jr, Jenni OG, Achermann P, et al. (2015) The Timing of the Circadian Clock and Sleep Differ between Napping and Non-Napping Toddlers. PLoS ONE 10(4): e0125181. https://doi.org/10.1371/journal.pone.0125181

# In[10]:


# Import the data (use this if running your Jupyter notebook within Coursera)
df = pd.read_csv("nap_no_nap.csv") 

df.head()
df


# In[11]:


# Imort the data (uncomment the line below and use this if you downloaded the Jupyter notebook)
df = pd.read_csv("https://raw.githubusercontent.com/UMstatspy/UMStatsPy/master/Course_2/nap_no_nap.csv")


# In[12]:


# First, look at the DataFrame to get a sense of the data
df


# **Question**: What variable is used in the column 'napping' to indicate a toddler takes a nap?  
# **Question**: What is the sample size $n$? What is the sample size for toddlers who nap, $n_1$, and toddlers who don't nap, $n_2$?

# ### Average bedtime confidence interval for napping and non napping toddlers
# Create two 95% confidence intervals for the average bedtime, one for toddler who nap and one for toddlers who don't.

# Before any analysis, we will convert 'night bedtime' into decimalized time.

# In[17]:


# Convert 'night bedtime' into decimalized time
df.loc[:,'night bedtime'] = np.floor(df['night bedtime'])*60 + np.round(df['night bedtime']%1,2 )*100

df.loc[df['napping'] == 1]


# Now, isolate the column 'night bedtime' for those who nap into a new variable, and those who didn't nap into another new variable. 

# In[18]:


bedtime_nap = df.loc[df['napping'] == 1]


# In[19]:


bedtime_no_nap = df.loc[df['napping'] == 0]


# Now find the sample mean bedtime for nap and no_nap.

# In[25]:


nap_mean_bedtime = np.mean(bedtime_nap.loc[:,'night bedtime'])

nap_mean_bedtime


# In[26]:


no_nap_mean_bedtime = np.mean(bedtime_no_nap.loc[:,'night bedtime'])

no_nap_mean_bedtime


# Now find the standard error for $\bar{X}_{nap}$ and $\bar{X}_{no\ nap}$.

# In[37]:


nap_se_mean_bedtime = sem(bedtime_nap.loc[:,'night bedtime'], ddof = 14)
nap_se_mean_bedtime


# In[38]:


no_nap_se_mean_bedtime = sem(bedtime_no_nap.loc[:,'night bedtime'], ddof = 4)
no_nap_se_mean_bedtime


# **Question**: Given our sample sizes of $n_1$ and $n_2$ for napping and non napping toddlers respectively, how many degrees of freedom ($df$) are there for the associated $t$ distributions?

# To build a 95% confidence interval, what is the value of t\*?  You can find this value using the percent point function: 
# ```
# from scipy.stats import t
# 
# t.ppf(probabiliy, df)
# ```
# This will return the quantile value such that to the left of this value, the tail probabiliy is equal to the input probabiliy (for the specified degrees of freedom). 

# Example: to find the $t^*$ for a 90% confidence interval, we want $t^*$ such that 90% of the density of the $t$ distribution lies between $-t^*$ and $t^*$.
# 
# Or in other words if $X \sim t(df)$:
# 
# P($-t^*$ < X < $t^*$) = .90
# 
# Which, because the $t$ distribution is symmetric, is equivalent to finding $t^*$ such that:  
# 
# P(X < $t^*$) = .95
# 
# So the $t^*$ for a 90% confidence interval, and lets say df=10, will be:
# 
# t_star = t.ppf(.95, df=10)
# 

# In[45]:


# Find the t_stars for the 95% confidence intervals
nap_t_star = t.ppf(.95, df=14)

nap_t_star


# In[41]:


no_nap_t_star = t.ppf(.95, df=4)

no_nap_t_star


# **Quesion**: What is $t^*$ for nap and no nap?

# Now to create our confidence intervals. For the average bedtime for nap and no nap, find the upper and lower bounds for the respective confidence intervals.

# **Question**: What are the 95% confidence intervals, rounded to the nearest ten, for the average bedtime (in decimalized time) for toddlers who nap and for toddlers who don't nap? 
# 
# CI = $\bar{X} \pm \ t^* \cdot s.e.(\bar{X})$

# **Challenge problem**: Write a function that inputs the column containing the data you want to build your confidence interval from and returns the confidence interval as a list or tuple (i.e. \[upper, lowe\] or (upper, lower)).
