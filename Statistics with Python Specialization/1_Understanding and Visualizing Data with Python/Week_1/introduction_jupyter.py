
# coding: utf-8

# ### What is Jupyter Notebooks?
# 
# Jupyter is a web-based interactive development environment that supports multiple programming languages, however most commonly used with the Python programming language.
# 
# The interactive environment that Jupyter provides enables students, scientists, and researchers to create reproducible analysis and formulate a story within a single document.
# 
# Lets take a look at an example of a completed Jupyter Notebook: [Example Notebook](http://nbviewer.jupyter.org/github/cossatot/lanf_earthquake_likelihood/blob/master/notebooks/lanf_manuscript_notebook.ipynb)

# ### Jupyter Notebook Features
# 
# * File Browser
# * Markdown Cells & Syntax
# * Kernels, Variables, & Environment
# * Command vs. Edit Mode & Shortcuts

# ### What is Markdown?
# 
# Markdown is a markup language that uses plain text formatting syntax.  This means that we can modify the formatting our text with the use of various symbols on our keyboard as indicators.
# 
# Some examples include:
# 
# * Headers
# * Text modifications such as italics and bold
# * Ordered and Unordered lists
# * Links
# * Tables
# * Images
# * Etc.
# 
# Now I'll showcase some examples of how this formatting is done:

# Headers:
# 
# # H1
# ## H2
# ### H3
# #### H4
# ##### H5
# ###### H6

# Text modifications:
# 
# Emphasis, aka italics, with *asterisks* or _underscores_.
# 
# Strong emphasis, aka bold, with **asterisks** or __underscores__.
# 
# Combined emphasis with **asterisks and _underscores_**.
# 
# Strikethrough uses two tildes. ~~Scratch this.~~

# Lists:
# 
# 1. First ordered list item
# 2. Another item
#   * Unordered sub-list. 
# 1. Actual numbers don't matter, just that it's a number
#   1. Ordered sub-list
# 4. And another item.
# 
# * Unordered list can use asterisks
# - Or minuses
# + Or pluses

# Links:
# 
# http://www.umich.edu
# 
# <http://www.umich.edu>
# 
# [The University of Michigan's Homepage](www.http://umich.edu/)
# 
# To look into more examples of Markdown syntax and features such as tables, images, etc. head to the following link: [Markdown Reference](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

# ### Kernels, Variables, and Environment
# 
# A notebook kernel is a “computational engine” that executes the code contained in a Notebook document. There are kernels for various programming languages, however we are solely using the python kernel which executes python code.
# 
# When a notebook is opened, the associated kernel is automatically launched for our convenience.

# In[ ]:


### This is python
print("This is a python code cell")


# A kernel is the back-end of our notebook which not only executes our python code, but stores our initialized variables.

# In[ ]:


### For example, lets initialize variable x

x = 1738

print("x has been set to " + str(x))


# In[ ]:


### Print x

print(x)


# Issues arrise when we restart our kernel and attempt to run code with variables that have not been reinitialized.
# 
# If the kernel is reset, make sure to rerun code where variables are intialized.

# In[ ]:


## We can also run code that accepts input

name = input("What is your name? ")

print("The name you entered is " + name)


# It is important to note that Jupyter Notebooks have in-line cell execution.  This means that a prior executing cell must complete its operations prior to another cell being executed.  A cell still being executing is indicated by the [*] on the left-hand side of the cell.

# In[ ]:


print("This won't print until all prior cells have finished executing.")


# ### Command vs. Edit Mode & Shortcuts
# 
# There is an edit and a command mode for jupyter notebooks.  The mode is easily identifiable by the color of the left border of the cell.
# 
# Blue = Command Mode.
# 
# Green = Edit Mode.
# 
# Command Mode can be toggled by pressing **esc** on your keyboard.
# 
# Commands can be used to execute notebook functions.  For example, changing the format of a markdown cell or adding line numbers.
# 
# Lets toggle line numbers while in command mode by pressing **L**.
# 
# #### Additional Shortcuts
# 
# There are a lot of shortcuts that can be used to improve productivity while using Jupyter Notebooks.
# 
# Here is a list:
# 
# ![Jupyter Notebook Shortcuts](img/shortcuts.png)

# ### How do you install Jupyter Notebooks?
# 
# **Note:** *Coursera provides embedded jupyter notebooks within the course, thus the download is not a requirement unless you wish to explore jupyter further on your own computer.*
# 
# Official Installation Guide: https://jupyter.readthedocs.io/en/latest/install.html
# 
# Jupyter recommends utilizing Anaconda, which is a platform compatible with Windows, macOS, and Linux systems.  
# 
# Anaconda Download: https://www.anaconda.com/download/#macos
