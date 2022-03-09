#!/usr/bin/env python
# coding: utf-8

# ## P04: Working with text files
# 
# ### Find a target string and then keep the next N lines of text
# * Here we will read in txt from a book (Frankenstein by Mary Wollstonecraft (Godwin) Shelley)
# * We'll then search for a specific string in the book...in this case we'll look for the first sentence of Chapter 5
# * We'll use `.readlines()` to read the book into a list, where each line of text from the book is an entry in the list (and remember, `.readlines()` is parsing the text based on where the `'\n'` (newline) characters are). 
# * Then we'll get rid of everything else in the book except for the few lines at the start of Chapter 5
# * I will show you two methods...one using a counter that we initialize, and one using the `enumerate` method that allows you to have a counter in a `for` loop that is initialized and incremented automatically. 
# * I'll also show you the `break` syntax for a `for` loop. `break` allows you to exit the loop if a certain condition is met. In this case, we will exit the loop when we find the text that we're looking for!
# * Last - there are many ways to do this task...so don't feel constrained by this approach when you're working on the problem set...

# In[1]:


# open our file for reading...
with open('frankenstein.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    # we'll call the list 'book'
    book = f.readlines()

# now we can search the book for the text that we want, 
# which in this case is the first sentence of Chapter 5, which 
# starts with the string 'It was on a dreary night' 
search_target = 'It was on a dreary night'

# how many lines of text do we want to keep 
# after we find the search target?
keep_lines = 50

# initialize a counter (int object)
cnt = 0

# loop over each line in the book
for line in book:
    
    # test to see if the current line has search_target in it
    if search_target in line:
        # grab the line where chapter 5 starts
        start_index = cnt
        
        # exit the for loop by calling 'break'
        break
        
    # if the current line does not have our search_target
    # then we'll increment the counter to keep track of how
    # many lines we've read...
    else:
        cnt += 1
        
# now use slicing to just keep the first keep_lines lines 
# after the search_target
book = book[start_index:start_index + keep_lines]

print(book)

# Related to ps3, Q1: How would you do the slicing if you 
# wanted to keep **all** of the text in the book after search_target?
# And how would do the slicing if you wanted to keep all of the text
# after the search_target while excluding the line that contained the 
# search_target? 


# ### Find a target string and then keep the next N lines of text but this time use `enumerate`
# * See [here](https://realpython.com/python-enumerate/) for a nice explanation...

# In[2]:


# open our file for reading...
with open('frankenstein.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    # we'll call the list 'book'
    book = f.readlines()

# now we can search the book for the text that we want, 
# which in this case is the first sentence of Chapter 5, which 
# starts with the string 'It was on a dreary night' 
search_target = 'It was on a dreary night'

# how many lines of text do we want to keep 
# after we find the search target?
keep_lines = 50

# loop over each line in the book using enumerate
# enumerate will automatically create and increment a counter 
# that we'll call 'cnt' and it will give you each line
# in the book just like a normal for loop. 
for cnt, line in enumerate(book):
    
    # test to see if the current line has search_target in it
    if search_target in line:
        # grab the line where chapter 5 starts
        start_index = cnt
        
        # exit the loop by calling 'break'
        break
        

# now use slicing to just keep the first keep_lines lines 
# after the search_target
book = book[start_index:start_index + keep_lines]

print(book)

# Related to ps3, Q1: How would you do the slicing if you 
# wanted to keep **all** of the text in the book after search_target?
# And how would do the slicing if you wanted to keep all of the text
# after the search_target while excluding the line that contained the 
# search_target? 


# ### Counting words in text...
# * Here we can count the occurence of each word in the book (or in the part of the book that you have left after slicing the book list in the code cell above). 
# * Notice that there are some empty strings `''` in the list that we need to deal with (i.e. things that are not words, so we need to check for these so they don't get counted). We can do that in a few ways that I'll write out below. 
# * Our general algorithm here will be: 
#     * convert the list to a string to make it easier to clean
#     * remove the newline characters using the `.replace()` method (and if you are working with a string that has other stuff in it that you don't want you can define a string with all the unwanted characters and loop over each_letter in that string to `.replace()` each unwanted character using a `for` loop). 
#     * convert back to a list
#     * initialize an empty dictionary
#     * loop over all unique words in the book - use `set` to get the unique words
#         * in this loop check to make sure we're not considering the empty strings `''`
#     * whenever we find a real word, create a new `key:value` pair in a dictionary with the word as the `key` and an initial value of `0`
#     * Now that the dictionary is set up and we have one key for each unique word, we can loop over **all** the words in the book, including repeated words, and increment the `value` associated with each `key`

# In[3]:


# turn the book list into a string to make it easier to remove things we don't want (like newline 
# characters)
book_str = ''.join(book)

# convert to lower case
book_str = book_str.lower()

# clean out the newline characters
book_str = book_str.replace('\n', ' ')

# turn back into a list based on the location of spaces
book_lst_clean = book_str.split(' ')

# init a dictionary with a key for each unique 
# word, and 0 for the starting count
wc = {}
for w in set(book_lst_clean):
    # because there are some empty strings in our list
    # we can check here and we'll skip them 
    if w != '':
        wc[w] = 0

# now loop over **all** words in the book, even the repeated words
# and count them up!
for w in book_lst_clean:
    if w != '':
        wc[w] += 1

# have a look at the dictionary...
print(wc)


# ### A slightly more compact way to count all the words in text using just one `for` loop
# * This might be easier to understand (or it might be harder) so just writing it out in case it helps...
# * I am using the `continue` statement (see below)...
# * Note that there are several other ways you could achieve the same result, so long as you are checking to make sure that the current word is not an empty string `''` somehow

# In[4]:


# turn the book list into a string to make it easier to remove things we don't want (like newline 
# characters)
book_str = ''.join(book)

# convert to lower case
book_str = book_str.lower()

# clean out the newline characters
book_str = book_str.replace('\n', ' ')

# turn back into a list based on the location of spaces
book_lst_clean = book_str.split(' ')

# init an empty dictionary
wc = {}   # or you can use dict()

# now loop over **all** words in the book, even the repeated words
# and count them up!
for w in book_lst_clean:
    
    # if w is not a word (i.e. it is an empty string)
    # then continue, where continue means "go back to the 
    # top of the for loop and skip the rest of the code in
    # the loop"
    if not w:
        continue
    
    # if w is a word, and its not already in our dictionary
    # then make a new key and assign a value of 0
    if w not in wc:
        wc[w] = 0
    
    # increment a counter each time the word w appears...
    # note that you only get to this line of code if w
    # is indeed a word (the if not w: continue
    # line above will prevent you from getting here if w is
    # not a word)
    wc[w] += 1

# have a look at the dictionary...
print(wc)


# ### Find the most common word in text. 
# * To find the most common word, you can loop over our word count dictionary (`wc`, defined above)
# * Basic approach: 
#     * Initialize a counter (lets call it `max_count`) to `0`
#     * Loop over `key:value` pairs in `wc` using the `.items()` method
#     * If the current `value` exceeds `max_count`, then update `max_count` with that value and also store the current `key`

# In[5]:


# init max_count to 0
max_count = 0

# loop over the key:value pairs in wc
for k,v in wc.items():
    
    # if the current value exceeds the previous value of 
    # max_count, then reassign max_count to the current value
    # and save the associated key (which is the actual word)
    if v > max_count:
        max_count = v
        most_common_word = k
        
print(f'The most common word is "{most_common_word}", it occured {max_count} times')
    

