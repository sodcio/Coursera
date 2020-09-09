
# coding: utf-8

# In[1]:


import math


# ## Data Types in Python 

# The following data types can be used in base python:
# * **boolean**
# * **integer**
# * **float**
# * **string**
# * **list**
# * **None**
# * complex
# * object
# * set
# * dictionary
# 
# We will only focus on the **bolded** ones

# Let's connect these data types to the the variable types we learned from the [Variable Types video](https://www.coursera.org/learn/understanding-visualization-data/lecture/iDodZ/variable-types).

# ###  Numerical or Quantitative (taking the mean makes sense)
# * Discrete
#     * Integer (int) #Stored exactly
# * Continuous
#     * Float (float) #Stored similarly to scientific notation. Allows for decimal places but loses precision.

# In[ ]:


type(4)


# In[ ]:


type(0)


# In[ ]:


type(-3)


# In[ ]:


#try taking the mean
numbers = [2, 3, 4, 5]
print(sum(numbers)/len(numbers))
type(sum(numbers)/len(numbers)) #In Python 3 returns float, but in Python 2 would return int


# **Floats**

# In[ ]:


3/5


# In[ ]:


6*10**(-1)


# In[ ]:


type(3/5)


# In[ ]:


type(math.pi)


# In[ ]:


type(4.0)


# In[ ]:


# Try taking the mean
numbers = [math.pi, 3/5, 4.1]
type(sum(numbers)/len(numbers))


# ### Categorical or Qualitative
# * Nominal
#     * Boolean (bool)
#     * String (str)
#     * None (NoneType)
# * Ordinal
#     * Only defined by how you use the data
#     * Often important when creating visuals
#     * Lists can hold ordinal information because they have indices

# **Boolean**

# In[ ]:


# Boolean
type(True)


# In[ ]:


# Boolean
if 6 < 5:
    print("Yes!")


# In[ ]:


myList = [True, 6<5, 1==3, None is None]
for element in myList:
    print(type(element))


# In[ ]:


print(sum(myList)/len(myList))
type(sum(myList)/len(myList))


# **String**

# In[ ]:


type("This sentence makes sense")


# In[ ]:


type("Makes sentense this sense")


# In[ ]:


type("math.pi")


# In[ ]:


strList = ['dog', 'koala', 'goose']
sum(strList)/len(strList)


# **Nonetype**

# In[ ]:


# None
type(None)


# In[ ]:


# None
x = None
type(x)


# In[ ]:


noneList = [None]*5
sum(nonList)/len(nonList)


# **Lists**
# 
# A list can hold many types and can also be used to store ordinal information.

# In[ ]:


# List
myList = [1, 1.1, "This is a sentence", None]
for element in myList:
    print(type(element))


# In[ ]:


sum(myList)/len(myList)


# In[ ]:


# List
myList = [1, 2, 3]
for element in myList:
    print(type(element))
sum(myList)/len(myList) # note that this outputs a float


# In[ ]:


myList = ['third', 'first', 'medium', 'small', 'large']
myList[0]


# In[ ]:


myList.sort()
myList


# There are more datatypes available when using different libraries such as Pandas and Numpy, which we will introduce to you as we use them.
