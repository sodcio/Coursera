
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Functions, lambda functions, and reading help documents

# We are going to introduce a few more python concepts. If you've been working through the NHANES example notebooks, you will have seen these in use already. There is a lot to say about these new concepts, but we will only be giving a brief introduction to each. For more information, follow the links provided or do your own search for the many great resources available on the web.  

# ### Functions
# 
# If you use a snippet of code multiple times, it is best practice to put that code into a function instead of copying and pasting it. For example, if you wanted several of the same plots with different data, you could create a function that returns that style of plot for arbitrary (though with correct dimension and type) data. 
# 
# In Python, indentation is very important. If done incorrectly, your code will not run and instead will give an error. When defining a function, all code after the ':' must be indented properly. The indentation conveys the scope of the code. [Some further explanation](https://docs.python.org/2.0/ref/indentation.html).
# ```
# def function_name(arguments):
#     """
#     Header comment: brief description of what this function does
#     
#     Args:
#         obj: input for this function
#     Returns:
#         out: the output of this function
#     """
#     
#     some code
#     
#     return out 
#  ```
#  
#  Exactly how to structure the header comments is up to you if you work alone, or will likely be specified if working for an established company. 
#  
# Function names should start with a lower case letter (they cannot start with a number), and can be in camelCase or snake_case.
# 
# If your function returns a variable, you use 'return' to specify that variable. A function doesn't always have to return something though. For example, you could have a function that creates a plot and then saves it in the current directory. 

# In[ ]:


def sum_x_y(x, y): # don't need comments if immediately clear what the function does
    out = x + y
    return out

sum_x_y(4, 6)


# In[ ]:


def get_max(x):
    current_max = x[0]
    for i in x[1:]:
        if i > current_max:
            current_max = i
    return current_max


# In[ ]:


get_max(np.random.choice(400, 100)) 
# np.random.choice(400, 100) will randomly choose 100 integers between 0 and 400       


# There is a lot more to be said about functions that we don't have time to cover in this course, so I leave you with examples of [common gotchas](https://docs.python-guide.org/writing/gotchas/) that you may run into.

# ### lambda functions
# 
# There are also know as anonymous functions because they are unnamed. This function can have any number of arguments but only one expression. Lambda functions, unlike defined functions, always return a variable.
# The format of a lambda function is  
# ```
# lambda arguments: expression  
# ```
# 
# They can look similar to a mathematical expression for evauating a function.  
# For example:
# ```
# (lambda x: x**2)(3)
# ```
# Is the same as mathmatically writing  
# $f(x) = x^2$ an then evauluating the function $f$ at $x=3$,  
# $f(3) = 9$

# In[ ]:


(lambda x: x**2)(3)


# Another way to use a lambda function is to store it in a variable like in the example below.

# In[ ]:


f = lambda x: np.sin(x)
x = np.linspace(-np.pi, np.pi, 100)
y = [f(i) for i in x]
plt.plot(x, y)
plt.show
# we could have made this several ways, can you think of another?


# You shouldn't come across many (if any) cases where you would have to use a lambda function, but we present them briefly here so that you can regonize them in the wild. 

# ### Reading help documentation
# A key skill in being a successful programmer is being able to read the documentation for a function and understand what that functions does and what the arguments are. 
# 
# To get the documentation, use the help function. First, let's call the help function on help, to see what is does:

# In[ ]:


help(help)


# We can see that calling help(thing) will print the documentation for 'thing'. Generally, this documentation will first list the function with its arguments (also called parameters), showing what the default arguments are. Then, it will list these arguments (parameters) and specify what they are and their type. Then it will documents what the function returns, errors it may raise, and possibly other documentation as necessary. Often, the bottom of the document will contain examples.
# 
# Let's look at another example, the pandas drop function. This is used to drop rows or columns from a DataFrame. If you had a DataFrame call 'my_df', you would call this function by
# ```
# my_df.drop(some arguments)
# ```
# Unfortunately, we cannot simply call 
# ```
# help(drop)
# ```
# because drop is not a function in base python. Instead, we must call
# ```
# help(pd.DataFrame.drop)
# ```
# because we need to specify that this is from pandas library (pd) and is applied to a DataFrame. If you're wondering why I'm capitalizing DataFrame as such, it is because that is a data type in the python pandas library. Without the capitalization, it had no meaning. 

# In[ ]:


help(pd.DataFrame.drop)


# If you wanted to drop the column 'this one' from the DataFrame 'my_df', how would you do it?
