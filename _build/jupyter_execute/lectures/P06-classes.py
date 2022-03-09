#!/usr/bin/env python
# coding: utf-8

# # P06: classes and objects
# 
# - objects
# - `class`
#     - attributes
#     - methods
# - instances
#     - `__init__`

# ## Objects and object oriented programming (OOP)
# 
# * Objects have special properties and data...these are referred to as **attributes** of an object
#     * **Methods**: Methods are functions that are defined for a specific object type
#     * **Data**: Some attributes of an object store data that is updated and stored in the object

# ### Storing Dates (Motivation)

# In[1]:


# A date, stored as a string
date_string = '29/09/1988'
print(date_string)


# In[2]:


# A date, stored as a list of numbers
date_list = ['29', '09', '1988']
date_list


# In[3]:


# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)


# In[4]:


# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary


# Ways to organize data (variables) and functions together.

# ### Example Object: Date

# In[5]:


# Import a date object
from datetime import date


# In[6]:


get_ipython().run_line_magic('pinfo', 'date')


# In[7]:


# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

# Create a date object
my_date = date(year, month, day)
print(my_date)


# In[8]:


# Check what type of thing `my_date` is
type(my_date)


# ## Accessing Attributes & Methods

# ### Date - Attributes
# 
# Attributes look up & return information about the object.

# **Attributes** maintain the object's data, or the object's state - these simply return information about the object to you...attributes are the data associated with an instance of an object 

# In[9]:


# Get the day attribute
my_date.day


# In[10]:


# Get the month attribute
my_date.month


# In[11]:


# Get the year attribute
my_date.year


# ### Date - Methods
# 
# * These are **functions** that **belong** to and operate on the object directly.
# * Methods modify the state of the object
# * Methods are accessed with a `.`, followed by the method name
# * Can get a list of all available methods by typing `object.` followed by the `tab` key

# In[12]:


# Method to return what day of the week the date is
my_date.weekday()


# In[13]:


# Reminder: check documentation with '?'
get_ipython().run_line_magic('pinfo', 'date.weekday')


# It's also possible to carry out operations on multiple date objects.

# In[14]:


# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)


# In[15]:


# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365, "years") #in years


# ### Listing Attributes & Methods : `dir`

# In[16]:


# tab complete to access
# methods and attributes
my_date.

# works to find attributes and methods
# for date type objects generally
date.


# In[17]:


## dir ouputs all methods and attributes
## we'll talk about the double underscores later in these notes...
dir(my_date)


# ### Objects Summary
# 
# - Objects allow for data (attributes) and functions (methods) to be organized together
#     - methods operate on the object type (modify state)
#     - attributes store and return information (data) about the object (maintain state)
# - `dir()` returns methods & attributes for an object
# - Syntax:
#     - `obj.method()`
#     - `obj.attribute`
# - `date` and `datetime` are two types of objects in Python

# ## Classes

# **Classes** define objects. The `class` keyword opens a code block for instructions on how to create objects of a particular type.

# Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They keep related things together and organized.
# 
# * See this [link](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) for more on Pascal case vs. snake_case (and other conventions)

# ## Example Class: Dog

# In[18]:


# Define a class with `class`.
# By convention, class definitions use CapWords (Pascal case)
class Dog():

    # Class attributes for objects of type Dog
    sound = 'Woof'

    # Class methods for objects of type Dog
    # default number of times assigned 2
    def speak(self, n_times=2):
        
        # we assigned the sound variable 
        # above and it belongs to this 
        # object...so we access that variable (attribute)
        # by calling self.attribute_name (self.sound in this case!)
        return self.sound * n_times


# A reminder:
# - **attributes** maintain the object's state; they lookup information about an object
# - **methods** usually alter the object's state; they run a function on an object

# **`class`** notes:
# 
# - classes tend to use **CapWords** convention (Pascal Case)
#     - instead of snake_case (functions and variable names)
# - `()` after `Dog` indicate that this is callable
#     - like functions, Classes must be executed before they take effect
# - can define **attributes** & **methods** within `class`
# - `self` is a special parameter for use by an object
#     - refers to the thing (object) itself
# - like functions, a new namespace is created within a Class
# 

# In[19]:


# Initialize a dog object
ricki = Dog()


# In[20]:


# ricki has the 'sound' attribute from the class Dog()
ricki.sound


# In[21]:


# ricki, has 'Dog' method(s)
# remember how we used `self` in our 
# method definition in the class Dog()
ricki.speak()


# ## Instances & self

# * An **instance** is particular instantiation of a class object. `self` refers to the current instance.
# * If you have two instances of an object, they can have different values for attributes...
#     * For example, if we wrote a variant of our `Dog()` class that keeps track of how many times it barks, then difference instances of `Dog()` can have different values for the attribute that keeps track of barking...

# In[22]:


# make a slightly more sophicated Dog...
class Dog():

    # Class attributes for objects of type Dog
    sound = 'Woof'
    barks = 0    # how many times has the Dog barked?
    
    # Class methods for objects of type Dog
    def speak(self, n_times=2):
        # update self.barks to keep track of
        # of how many woofs...
        self.barks += n_times
        
        # then make the sound the desired number of times
        return self.sound * n_times


# In[23]:


# Initialize two instances of class Dog()
ricki = Dog()
punky = Dog()


# In[24]:


print(f'First ricki says: {ricki.speak(5)}')
print(f'Then punky responds: {punky.speak(2)}')
print(f'Ricki agrees to chase the rabbit by saying: {ricki.speak(2)}')


# In[25]:


print(f'Punky barked {punky.barks} times during the conversation')
print(f'Ricki barked {ricki.barks} times during the conversation')


# From our example above:
# 
# - Dog is the Class we created
# - `ricki` is one _instance_ of the class, `punky` is another _instance_
# - The class Dog has two attributes - sound ('Woof') and `barks` (number of times each **instance** of Dog has barked)
# - `self` refers to whatever the _current_ instance is...

# 
# ## Instance Attributes
# 
# An instance attribute specific to the instance we're on. This allows different instances of the same class to be unique (have different values stored in attributes and use those in methods).

# In[26]:


# Initialize an empty list to store a pack of dogs
pack_of_dogs = []

# make 4 instances of Dog()
for dog in range(4):
    pack_of_dogs.append(Dog())
    
# note that all instances of Dog()
# have the same attributes (sound and barks)
# e.g. all Dogs say 'Woof'
for dog in pack_of_dogs:
    print(dog.sound)


# This creates four different `Dog` type objects and stores them in a list. So even though we could separately keep track of how many times each dog barked, every dog starts with the same two attributes (`sound` and `barks` and they all start off being assigned `'Woof'` and `0`...

# What if we want to have attributes that are different for diffgerent instances of a class? 
# 
# These are called **instance attributes** and `__init__` is a special method used to define them.
# 
# ## Example Class: Dog Revisited
# 
# - Two trailing underscores (a `dunder`, or double underscore) is used to indicate something Python recognizes and knows what to do every time it sees it.
# - Here, we use `__init__` to execute the code within it every time you initialize an object.

# In[27]:


class Dog():

    # Class attributes for *all* Dogs
    # these are shared by all instances 
    # of Dog
    sound = 'Woof'
    barks = 0
    
    # __init__ method allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    # in this case we can give each instance of Dog a different name...
    def __init__(self, name):
        self.name = name

    def speak(self, n_times=2):
        self.barks += n_times
        return self.sound * n_times


# In[28]:


# Initialize a dog
# what goes in the parentheses is defined in the __init__
dog1 = Dog(name='Ricki')
dog2 = Dog(name='Punky')


# In[29]:


# Check dog1's attributes
print(dog1.sound)    # This is an class attribute
print(dog1.name)     # This is a instance attribute


# In[30]:


# Check dog2's methods
dog2.name


# ## Everything in Python is an Object!

# ### Data variables are objects

# In[31]:


print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))


# ### Functions are objects

# In[32]:


print(isinstance(sum, object))
print(isinstance(max, object))


# In[33]:


# Custom function are also objects
def my_function():
    print('yay Python!')

isinstance(my_function, object)


# ### Class definitions & instances are objects

# In[34]:


class MyClass():
    def __init__(self):
        self.data = 13

my_instance = MyClass()

print(isinstance(MyClass, object))
print(isinstance(my_instance, object))


# ## More complex example
# * Here we'll make something a little more complex and useful...this will be a `RealEstate` object that keeps track of how much money you have and whether you want to buy or sell a property. 
#     * You start with `seed_money` dollars - this will be stored in the attribute `money` and `seed_money` will be defined when you create an instance of `RealEstate`. 
#     * You also start with an empty dictionary named `properties` that will store the address, size (in sq ft) and cost of properties that you purchase and now own. 
#     * Based on your real estate acumen, you will buy any property that is over 1900 sq ft in size as long as it costs less than 1 million dollars. If it over 1900 sq ft and costs more than 1 million dollars, you will not buy it. 
#     * You will have a method that determines whether you will buy the house, we'll call this method `purchase`
#     * We will pass `purchase` the address of the house, the house size (in sq ft) and the cost. 
#     * If the house satisfies your criteria, **and you have enough money**, then you will buy the house, subtract the cost of the house from the `money` attribute, and you will update the `properties` dictionary. 
#     * If the house meets the size and cost requirements, but you do not have enough money, print the message `"Sorry - nice house but you don't have enough money"`
#     * If the house does not meet your criteria, then print `"Not interested"`
# 

# In[35]:


class RealEstate():
    
    # Init instance attributes 
    def __init__(self, params):
        
        # initialize a dictionary to store 
        # address, size, cost of purchased properties
        self.properties = dict()
        
        # initialize seed_money, default is 0
        self.money = params.get('seed_money', 0)
        
        # initialize min_size of house, default is 1000
        self.min_size = params.get('min_size', 1000)
        
        # initialize max_price, default is 500000
        self.max_price = params.get('max_price', 500000)
                
            
    # purchase method to determine if  you buy, update dictionary, etc. 
    def purchase(self, address, size, cost):
        
        # see if the size is acceptable, if the cost is acceptable, and if we 
        # have enough money...
        if size >= self.min_size and cost <= self.max_price and self.money>=cost:
                        
            # subtract the cost from total amount of money
            self.money -= cost
            
            # update dictionary
            self.properties['address'] = address
            self.properties['size'] = size
            self.properties['cost'] = cost
            
            print(f'You now own: {address}')
        
        elif size >= self.min_size and cost <= self.max_price and self.money <= cost:
            print("Sorry - nice house but you don't have enough money")
        
        else:
            print("Not interested - too small or too much money!")


# In[36]:


# create an instance of RealEstate
params = {'seed_money' : 3000000, 'min_size' : 1900, 'max_price' : 1000000}
re = RealEstate(params)

# check to make sure we initialized everything correctly in __init__
print(re.money)
print(re.properties)
print(re.max_price)


# ### Now we can pass in some properties to see if we want to buy them...

# In[37]:


re.purchase('203 N Amity St. Baltimore, MD, 21223', 2100, 999000)


# In[38]:


# see if we decremented our money correctly
print(re.money)
print(re.properties)


# In[39]:


# See what happens when our criteria are not met - cost too high
re.purchase('110 Calle Iglesia, San Clemente, CA 92672', 2100, 4000000)


# In[40]:


# Buy another one to run down our money...
re.purchase('9826 La Jolla Farms Rd La Jolla, CA', 10500, 999999)
re.purchase('2808 Ocean Front, Del Mar, CA, 92014', 5800, 900000)


# In[41]:


# check our cash...
re.money


# In[42]:


# now try to buy a house that meets our criteria but that we can't afford...
re.purchase('9630 La Jolla Farms Rd, La Jolla, CA 92037', 3290, 875000)


# ## Data analysis example
# * recall the functions that we used for cleaning text...lets write a class that can do all of those operations for us!

# In[43]:


class CleanText():
    
    def __init__(self, params):
        
        # if search target is defined...else ''
        self.search_target = params.get('search_target', '')
        
        # keep how many lines after search target? 
        # default 0 which will mean "keep till end of book"
        self.keep_lines = params.get('keep_lines', '')
        
        
    # segment text...
    def segment_text(self, text):
        
        for cnt, line in enumerate(text):
    
            # test to see if the current line has search_target in it
            if self.search_target in line:
                # grab the line where chapter 5 starts
                start_index = cnt
        
                # exit the loop by calling 'break'
                break
        
        # slice
        if self.keep_lines:
            text = text[start_index:start_index + self.keep_lines]
        else: 
            # go from start to end of book
            text = text[start_index:]
            
        return text
    
    
    # turn to lower case 
    def clean_text(self, text):
        # join text list into a string
        text_string = ' '.join(text)
        
        # lower case it
        text_string = text_string.lower()
        
        # remove newlines
        text_string = text_string.replace('\n', '')

        # remove all unwanted characters (punctuation...)
        for c in set(text_string):
            if c not in ' abcdefghijklmnopqrstuvwxyz':
                text_string = text_string.replace(c, '')
        
        # convert back to list...
        return text_string.split(' ')

    
    # count the words...
    def count_words(self, text):
        
        # first clean the text...
        text = self.clean_text(text)
        
        # then count the words!
        wc = {}   # or you can use dict()

        # now loop over **all** words in the book
        for w in text:

            # if w is not a word (i.e. it is an empty string)
            # then continue
            if not w:
                continue

            # if w is a word, and its not already in our dictionary
            # then make a new key
            if w not in wc:
                wc[w] = 0

            # increment a counter each time the word w appears...
            wc[w] += 1
            
        return wc


# In[44]:


# open our file for reading...
with open('frankenstein.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    # we'll call the list 'book'
    text = f.readlines()


# In[45]:


# set up our object...specifying search target but not keep lines 
# (will use the default value for that...)
params = {'search_target': 'It was on a dreary night'}
ct = CleanText(params)
ct.search_target


# In[46]:


# segment text
text = ct.segment_text(text)
print(text)


# In[47]:


# count the words!
wc = ct.count_words(text)
print(wc)


# In[48]:


# importantly - this class can handle processing any text!
with open('alice-in-wonderland.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    # we'll call the list 'book'
    text = f.readlines()


# In[49]:


# set up our object...specifying search target but not keep lines 
# (will use the default value for that...)
params = {'search_target':'Down the Rabbit-Hole', 'keep_lines':100}
ct = CleanText(params)
ct.search_target


# In[50]:


# segment text
text = ct.segment_text(text)
print(text)


# In[51]:


# count the words!
wc = ct.count_words(text)
print(wc)


# ## Importing a class that you've defined
# * Once you have written a class to define an object, you can import it and use it in any of your other projects without re-typing all the code or copying and pasting it into a notebook...
# * Here we can use the writefile cell magic to write a text file with our code ( a .py file is just a text file that is associated with python code). 

# In[52]:


get_ipython().run_cell_magic('writefile', 'MyMath.py', 'class MyMath():\n    \n    def multiply(self, num1, num2):\n        return num1 * num2\n        \n    def minus(self, num1, num2):\n        return num1 - num2\n    \n    def add(self, num1, num2):\n        return num1 + num2\n    \n    def divide(self, num1, num2):\n        return num1 / num2 \n    \n    # of course we have a built-in ** operator \n    # to do this, but see how we can call another \n    # method in this class using self...\n    def square(self, num1):\n        return self.multiply(num1, num1)')


# ### Now we can import the object and use it...

# In[53]:


# import the contents of the file...* means "everything"
from MyMath import *

# make our object...
mm = MyMath()

# then we can use it!
mm.square(10)


# 
# ## Classes Review
# 
# - `class` creates a new class type
#     - names tend to use CapWords case
#     - can have attributes (including instance attributes) and methods
#         - `obj.attribute` accesses data stored in attribute
#         - `obj.method()` carries out code defined within method
# 

# - instance attributes defined with `__init__`
#     - `__init__` is a reserved method in Python
#     - This "binds the attributes with the given arguments"
#     - `self` refers to current instance

# - to create an object (instance) of a specified class type (`ClassType`):
#     - `object_name = ClassType(input1, input2)`
#     - `self` is not given an input when creating an object of a specified class
