#!/usr/bin/env python
# coding: utf-8

# # P02: While loops
# 
# ## While Loops
# 
# 
# A **while loop** is a procedure to repeat a piece of code while some condition is still met.

# `while` loops always have the structure:
# 
# ```python
# while condition:
#     # Loop contents
# ```
# 
# While condition is true, execute the code contents.
# 
# Repeat until condition is no longer True.

# ## While Loops

# In[1]:


number = 10

while number >= 0:
    print(number)
    number = number - 1


# ### Infinite loops
# 
# While loops are a great way for beginners to shoot themselves in the foot:
# it is very easy to introduce a slight bug that causes the while condition to always evaluate to true, and thus the while loop will never stop.  When this happens, you have to stop the python kernel/interpreter, and start over.  For this reason, you should not use while loops unless you have a very good reason to do so.  For-loops are preferable!
# 
# Examples of while loops that never end:
# 
# ```python
# number = 10
# while number >= 0:
#     print(number)
# 
# number = number - 1
# ```
# 
# ```python
# number = 10
# while number >= 0:
#     print(number)
#     number = number + 1
# ```
# 
# ```python
# number = 0
# while number <= 0:
#     print(number)
#     number = number - 1
# ```
# 
