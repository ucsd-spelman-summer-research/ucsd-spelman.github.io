#!/usr/bin/env python
# coding: utf-8

# # P04: Dictionaries
# - **Concepts**: ordered vs not
# - **Initializing and indexing**
# - **Python dict**: dict, .update(), del

# 
# ## Dictionaries
# 
# 
# Dictionaries are *unordered*, *mutable*, *collections*, of *key*-*value* pairs.  They are a mapping from *distinct* keys, onto values.
# 
# In Python dictionaries are like lists in that they:
#  - are *mutable* (so you can change them),
#  - are *collections* of other objects (so you can iterate over them, get their `len()`, check membership with `in`).
#  - you can get items with square brackets `[]` (but not with integer index)
# 
# However, they are unlike lists in that:
# - they are *unordered* so they cannot be indexed with integers or sliced.
# - the are *mappings* between *distinct* keys and values.
# 
# Dictionaries are created with `dict()`, or with `{key:value}` notation or by just initializing an empty dictionary with `{}`

# ### Init using `dict()` 

# In[1]:


courses = dict() 
courses['CSS2'] = 'Data/Model Python'
courses['CSS1'] = 'Intro Python'
print(courses)


# ### Two alternate ways to achieve the same thing as above
# * Init with `{}` and then fill like we did above
# * Init with `{key:value}` pairs

# In[2]:


# init with {} and then fill (just like we did above)
courses = {} 
courses['CSS2'] = 'Data/Model Python'
courses['CSS1'] = 'Intro Python'
print(courses)


# In[3]:


# directly assign key:value pairs upon creation
courses = {'CSS2': 'Data/Model Python', 'CSS1': 'Intro Python'}


# ### Dictionary elements can be accessed via their keys.

# In[4]:


print(courses['CSS1'])


# ### Items can be added to dictionaries by assigning to new keys,

# In[5]:


courses['ABB'] = 'Is this a course?'
print(courses)


# ### Dictionaries can be updated with `.update()`, which will add new keys, and update the values of existing keys.

# In[6]:


new_courses = {'ABB': 'this is not a course', 'CSS100':'Analytic Programming'}
courses.update(new_courses)
print(courses)


# ### Elements of dictionaries can be deleted with the `del` keyword:

# In[7]:


del courses['ABB']
print(courses)


# You can check if a key exists in a dictionary with `in`:

# In[8]:


print('CSS1' in courses)
print('ABB' in courses)


# 
# 
# ## Keys, Values, Items

# ### You can get (or iterate over) just the keys with `.keys()`.

# In[9]:


print(courses.keys())
for k in courses.keys():
    print(k)


# ### You can get just the values with `.values()`.

# In[10]:


print(courses.values())
for v in courses.values():
    print(v)


# ### You can get key-value pairs (as tuples) with `.items()`.

# In[11]:


print(courses.items())
for pair in courses.items():
    print(pair)


# ### It is often useful to do **assignment unpacking**, or to unpack the (key,value) tuple into two variables
# * This is super handy because then you have access to both the key and the value inside of the for loop
# * By convention use the variables `k` and `v` to improve readability, but remember that you can use any variable name you want...

# In[12]:


for k,v in courses.items():
    print(f'Course number {k} is titled {v}')


# ## Sorting
# 
# As you saw above, the order of key-value pairs in a dictionary is determined by when they were added.  Often we want to sort the contents either by the keys, or by the values.   
# * To get a sorted dictionary, we will end up making a new dictionary by inserting key-value pairs in a sorted order.

# ### Here is an exmaple of sorting **By keys**

# In[13]:


sorted_courses = dict()
for k in sorted(courses.keys()):
    sorted_courses[k] = courses[k]

print(courses)
print(sorted_courses)


# ### Here is an exmaple of sorting **By values**
# 
# Sorting by values is a bit tricky -- we can sort the values, but we have no reliable way to figure out which keys were associated with the sorted values.  Consequently, we have to sort the key-value items.  But doing so requires that we can tell the `sorted` function to use the second element of the pair to sort.  This is all doable, but involves a lot of extra coding...
# 
# Instead, we will use the `itemgetter` function from the `operator` library
# * The default is for `sorted` to sort by keys...`itemgetter` will allow you to sort by values
# * Note that in a given `{key:value}` pair that the key is in the 0th index and the value is in the 1nth index...just noting that for now, but you'll see why this is important when we use `itemgetter`
# 
# 
# * And one side-note that this is the first time that we've covered importing extra functionality from a library.
# * You will use this more and more often as there are many libraries that expand the core functionality of python (e.g., NumPy, Pandas, Matplotlib, etc). 
# * We will cover those in the coming weeks, and will also cover more about how to do imports. 

# In[14]:


# this imports the itemgetter function
# remember that once you import something
# it is available to all other code cells
# in the notebook...so run this cell first
# and then you'll have access to `itemgetter` 
# in all the other cells...
from operator import itemgetter 


# In[15]:


print("before sorting, items in order of insertion:  ")
for item in courses.items():
    print(item)

print("default sorting sorts by first element of pair (key):  ")
for item in sorted(courses.items()):
    print(item)

# we're sorting by the 1nth index in the {key:value} pairs, which is the value..
# see what happens if you use itemgetter(0)- then it will sort by the keys!
print("sorting by the second element (index=1) of the pair with key=itemgetter(1):  ")
for item in sorted(courses.items(), key=itemgetter(1)):
    print(item)


# ## Bonus and advanced syntax...making a new sorted dictionary using a normal `for` loop and using a **dictionary comprehension**

# ### Make a new dictionary that contains sorted items of the old dictionary using a for loop...

# In[16]:


courses_by_title = dict()

for number,title in sorted(courses.items(), key=itemgetter(1)):
    courses_by_title[number] = title

print(courses_by_title)


# ### Make a new dictionary that contains sorted items of the old dictionary using a dictionary comprehension. This is a compact way of achieving the same thing that the standard `for` loop did above...

# In[17]:


courses_by_title = {k:v for k,v in sorted(courses.items(), key=itemgetter(1))}
print(courses_by_title)

