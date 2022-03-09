#!/usr/bin/env python
# coding: utf-8

# # P04: Reading and writing files
# - **Python files**: open, close, with open as fp
# 
# 
# ## Reading files
# 
# ### Finding a file
# 
# - Files are stored somewhere in your computer systems hard drive or storage area.
# 
# - That location is specified via a file **path**.
# 
# - A file path encodes the location of the file within the directory structure on the computer.
# 
# - *Absolute* file paths encode the location of the file relative to the root, or base directory of the file system.  So let's say we have a file named `filename.ext` located in `folder2`, which is located inside `jserences`, which is inside `Users`, which is in the base (root) directory of the file system.  On a unix machine (such as Mac OS, Linux, etc.) this location is encoded as follows `/Users/jserences/folder2/filename.ext` where the slashes (`/`) indicates directories or folders. Windows machines use the forward slash `\`, so that path would look something like `C:\Users\jserences\folder2\filename.ext`.
# 
# - *Relative* file paths encode the location of the file relative to the current location or path, where the program is running. So if a program has been launched in the folder `/Users/jserences/programs/`, then the relative path to `/Users/jserences/folder2/filename.ext` would involve going up one directory in the file tree using the `..` syntax, then down into `folder2` and getting `filename.ext`.  The full relative path would be `../folder2/filename.ext`.  The key part here is that `..` move you up one level in the directory tree **relative** to the the current working directory. Basically `..` is like pressing the `back` arrow on a 'Finder' window when you're moving around using the mouse and the windows provided by your operating system.
# 
# ### Opening a file
# 
# - Files are accessed via the `open(file, mode)` command, specifying the (relative or absolute) path to the  file, and the mode with which you want to open it ('r' for read, 'w' for write, 'a' for append, there are [more](https://docs.python.org/3/library/functions.html#open)).
# 
# - Opening a file creates a file object which can be read from (or written to, or appended to, depending on what mode you used to open it).  
#     - Assuming we are dealing with text files, `file.read()` reads the entire content of the file as one string. 
#     - `file.readlines()` reads the entire content of the file as a list of strings, with each element corresponding to one line in the text file.  
#     - `file.readline()` reads one line at a time, and is helpful if your file is large, and you do not want to load its entirety into memory.
# 
# - When you open a file, your operating system is notified that some program is doing something to that file, and it will prevent other changes from being made to that file. Consequently, it is important that you *close* the file after opening it.  In Python, the easiest way to make this that this is done without errors is via the `with` keyword, that creates a temporary context in which the file is open, and then closes the file as soon as all the operations that need to be carried out on the file are completed. Bad things can happen if you do not close the file, so make sure you're careful with this (the file might get corrupted, you might find that nothing was written to the file, etc). 

# ## File Paths

# The specific location of a file or folder on your computer.

# When using a Graphical User Interface (GUI), you click on directories to access subdirectories and finally find the file you're interested in.

# When using the command line, you specify a file's path explicitly with text.

# ### Absolute vs. Relative Paths
# 
# The two ways to specify the path to your file of interest allow for flexibility in programming.

# #### Absolute Paths

# Absolute paths specify the full path for a given file system (starting from the root directory).

# **root** specifies the 'highest' directory in the file structure (the start).
# 
# An absolute file path starts with a slash `/` specifying the root directory.
# 

# In[1]:


## absolute path
## this is specific to my computer
## look at the path output above for you computer
get_ipython().run_line_magic('ls', "'/Users/johnserences/Dropbox/My Papers/Editorial/'")


# #### Relative Paths

# **Relative paths** specify the path to a file from your **current working directory** (where your computer is working right now).
# 

# In[2]:


# remind us of our current working directory
get_ipython().run_line_magic('pwd', '')


# In[3]:


# relative path
# this is specific to my computer
get_ipython().run_line_magic('ls', '../../Lectures')


# - `..` specify you want to move one directory up in your hierarchy - here I am moving up two levels with the `../../` syntax
# - `Lectures` specifies the path to the directory I want to list files in
# - each directory is separated with a slash (`/`)

# This **relative** path does _not_ start with a leading slash (b/c it's not an absolute path).

# ## Opening and interacting with files!
# * Using the `with` method of opening files will ensure that they are closed properly when you are done with them...
# * This will create a file object `f` (although you can name it whatever you'd like)
# * You can then use the file object `f` to write stuff to the file using `f.write()`

# ### Open a file for writing, and just write some text to it using the f-string method we learned last time...

# In[4]:


with open('test.txt', 'w') as f:
    for i in range(0, 11):
        # include the \n newline character.
        # its like pressing the `enter` key at the end of each line
        f.write(f'This is the {i}th line of the file\n')


# Note the escape sequence `'\n'` in the strings -- these are the *newline* escape character, and is how we encode line breaks inside strings.

# ### You can use the built in magic `%pycat` to view the contents of the file. 

# In[5]:


get_ipython().run_line_magic('pycat', 'test.txt')


# ### Open a file for reading...
# * `f.read()` will read in a fixed number of elements...where `f.read(x)` will read in `x` elements
# * if not parameters are passed to `f.read()` then it will read the entire file! be careful with this if you're dealing with super big files!
# * `f.readline()` will read in one line at a time (and it knows how to find the end of each line because its looking for the the `\n` newline escape character...that's why it is so important to include the `\n` in your files when you write them...makes it way easier to deal with when reading the data back in. 
# * `f.readlines()` will read in the entire file and will store each line as a string that is an entry in a list...

# #### `f.read()`

# In[6]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read the entire file...
    out = f.read()
    
# print it out
print(out)


# #### This time use `f.read() but specify a fixed number of elements to read (instead of the entire file). 

# In[7]:


# make a variable to determine how many elements to read.
num_elements_to_read = 10

# open our file for reading...
with open('test.txt', 'r') as f:
    # This time just read in a set number of elements
    out = f.read(num_elements_to_read)
    
# print it out - note that there are 
# num_elements_to_read characters (including spaces)
print(out)


# ### `f.readline` - read one line

# In[8]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read a line from the file
    out = f.readline()
    
# print it out
print(out)


# #### Side note, but sorta related to `f.readline()`...if you want to loop over lines, one at a time, use a for loop like this:

# In[9]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read in line by line...
    for line in f:
        print(line, end="")
        # end = "" tells the `print` statement not to end each 
        # line with a '\n' because there is already a '\n' character
        # at the end of each line because that is how we wrote it out...


# ### `f.readlines()` - read entire file into a list of strings, where each string is a line from the file. 

# In[10]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    out = f.readlines()
    
# print the list of strings
print(out)

# because `out` is now a list, 
# you can index/slice to find specific 
# elements
print('\nSlicing the list to grab a subset of the strings...\n')
print(out[2:4])

