#!/usr/bin/env python
# coding: utf-8

# # P01: Our environment
# 
# ## Jupyter Notebooks
# 
# This is a jupyter notebook.  A notebook is file that combines explanatory text (written in markdown), computer code, and the output of the computer code.  
# 
# A notebook is comprised of "cells".  A given cell can contain different types of things.  We will concern ourselves with cells that contain either markdown (like this cell), or python code.  

# ### Markdown Cells
# 
# Markdown is a way of specifying text formatting in plain text.   
# For instance, this cell starts with the text `### Markdown` which tells the computer that it should display a level 3 heading with the text "Markdown".  The cell above starts with the text `# CSS 1:...` which specifies a level 1 heading, which you can see is rendered in larger text.
# 
# Some other common markdown formatting syntax:   
# 
# #### paragraphs and linebreaks
# 
# Markdown ignores single line breaks. For instance, the following markdown is rendered on one line:
# 
# ```markdown
# The text here
# is 
# formatted
# like so.
# ```
# 
# The text here
# is 
# formatted
# like so.
# 
# To create linebreaks you can either add two linebreaks between each line, like so:
# 
# 
# ```
# The text here
# 
# is 
# formatted
# like so.
# ```
# 
# The text here
# 
# is 
# formatted
# like so.
# 
# 
# Or you could add two spaces to the end of each line:
# 
# ```
# The text here  
# is   
# formatted   
# like so.  
# ```
# 
# The text here  
# is   
# formatted   
# like so.  
# 
# 
# 
# #### text formatting
# 
# `*text*` yields italics: *text*   
# `**text**` yields bold: **text**   
# ``` `text` ``` yields a code formatting: `text`
# 
# 
# #### links
# 
# `[text](URI)` yields a link.  For instance `[pydocs](https://docs.python.org/3/)` yields a link to python docs: [pydocs](https://docs.python.org/3/)
# 
# #### lists
# 
# ```
# - item 1  
# - item 2
# ```
# 
# yields a bulleted list:
# - item 1   
# - item 2
# 
# ```
# 1. item 1  
# 2. item 2
# ```
# 
# yields an automatically numbered list:
# 
# 1. item 1  
# 1. item 2
# 
# 

# ### Code cells
# 
# The virtue of jupyter notebooks is that you can mix explanatory text with computer code, and the results of running that code.  We will be using these notebooks with Python code.  Python code will run in special kinds of cells called code cells.
# 
# A given code cell has some content, which is sent to a Python interpreter.  Upon executing that code, the cell prints some output.  The output may be more or less complicated.  Without any particular instructions about what to output, the code cell will output whatever the last line "returns"

# In[1]:


34


# #### Magics 
# 
# We will spend most of our time worrying about how to write code that goes inside code cells, but it is worth noting that code cells can also contain special commands called "line magics" or "cell magics" which do something, but are not part of the python language itself.  These commands occur on lines starting with `%` or `%%`.  We will cover them as needed, but for now, here is an example:   
# 
# `%lsmagic` will list all the line and cell magics that are available.

# In[2]:


get_ipython().run_line_magic('lsmagic', '')


# ### Notebook navigation
# 
# Notebooks are "modal" in the sense that you can be in different modes.  If you are in "edit" mode, you are editing the content of a given cell.  If you are in "command" mode then you might create new cells, change their type, rearrange them, etc.
# 
# You can enter command mode by hitting "escape".  Then you can navigate with the arrow keys, or by clicking on particular cells.  
# 
# You can enter "edit" mode in a given cell by pressing the "enter/return" key.  
# 
# When in edit mode, you can press "Shift + enter" (hold down the shift key and press enter) to execute the cell, and exit edit mode.
# 
# In command mode, you can press "H" to see a list of keyboard shortcuts, or you can press "cmd + shift + f" to enter the command pallette, where you can search for all the commands available to you.
# 
# There is a lot of extended functionality to notebook navigation and execution, but that covers the basics.

# ### Kernel
# 
# A notebook is edited in a browser, but it "talks" to a "kernel" that is being run on some server.  The Kernel is a running session of (in our case) Python.  When we run a code cell in the notebook, the code from that cell is sent to the running Python kernel, which executes that code, and then sends the output back to the notebook.  The notebook then embeds that output below the code cell.
# 
# This arrangement is rather complicated.  It has a number of benefits and a number of costs.
# 
# The benefits: The output has to be run once, and is then embedded in the notebook, and can be viewed without rerunning the code.  The code can be embedded in a document such as this one, with text, explanations, output, etc.  The kernel can be run on various remote servers, while you access the notebook through your own browser, so you do not have to set up your own python environment on your own computer, and so you can easily plug into a kernel running on a server more powerful than your own computer.
# 
# There are costs however: Code cells can be executed out of order, and the state of the kernel is changed by each cell that is run.  This can cause quite a bit of confusion.   A notebook is a complicated file, and you can't just look at it in a text editor, as you could would just code on its own. 

# 
