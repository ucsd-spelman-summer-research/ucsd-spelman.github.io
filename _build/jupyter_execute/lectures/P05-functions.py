#!/usr/bin/env python
# coding: utf-8

# # P05: Functions
# * **Concepts**: abstraction, functions, scope, mutable/immutable
# * **Python functions**: writing, scope, pass by reference implications

# ## Intro to functions 
# 
# A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
# * If you ever find yourself writing out (or copying/pasting) the same bit of code more than once, you should consider making it a function that you can call whenever you need to perform a given operation...
# * Saves a ton of time and reduces the chance of making an error
# 
# **Modular Programming**
# 
# Modular programming is an approach to programming that focuses on building programs from independent modules ('pieces').
# 
# * defining a function
#     * `def`
#     * `return`
#     
# * executing a function
#     * parameters
#     * local and global namespaces

# ## Functions for Modular Programming

# - Functions allow us to flexibly re-use pieces of code
# - Each function is independent of every other function, and other pieces of code
# - Functions are the building blocks of programs, and can be flexibly combined and executed in specified orders
#     - This allows us to build up arbitrarily complex, well-organized programs

# In[1]:


# you've seen functions before
# recall that built in functions like print()
# will turn green when you type them
my_var = [3, 4, 5]

# print the second item to the end
print(my_var[1:])


# ## Creating your own function
# 
# * When you use `def` you are creating a **user-defined function**.
# * After `def` you give the function a name (something meaningful)
# * Then you have `()` where you can pass arguments into the function
# * These input arguments contain information that the function needs to produce the desired output
# * Remember to `return` the output of the function! Sometimes a function can modify an object **in place**, but far more often the function will do some operation and then you need to return the output of that operation so that you can use it elsewhere in your code
# * Remember to run the code cell that contains the function...if you don't run the code cell then it won't be available to call from other code cells in your code. 

# In[2]:


# define a function named double_value
# it will take a number and double the value
# num is the input parameter for the function
def double_value(num):

    # double the value of num
    doubled = num + num

    # return output from function
    # this is super important!
    # if you don't return the value 
    # then nothing will actually 
    # happen
    return doubled


# ### Keyword arguments when excecuting a function 
# * Note that built-in python functions turn green when you type them, but your custom made function will not
# * You can specify the input using **keyword** arguments where you explicitly assign the input argument by name (e.g. `double_value(num=6)` where you explicitly define `num=6`)

# In[3]:


double_value(num=6)


# ### Positional arguments when excecuting a function
# * You can also pass arguments by position (positional arguments) in which case the order of entry determines what values get assigned to each input argument. 
# * Here we only have one argument (`num`) so there is no chance for confusion, but if you have multiple arguments in a more complex function then it is essential that you get the input order correct when using positional arguments and it is a good habit to use keyword arguments...more on this below

# In[4]:


double_value(6)


# ## Creating a function with multiple inputs
# * Something *slightly* more interesting than just adding a value with itself
# * This function will add two numbers together and then it will `return` the output
# * Note that it has two input arguments `num1` and `num2`
# * Remember to run the function so that you 

# In[5]:


def add_two_numbers(num1, num2):

    # Add the two input variables together
    # and assign to the varible answer
    answer = num1 + num2

    # Return answer
    return answer


# ### Call the function using keyword arguments

# In[6]:


output = add_two_numbers(num1=1, num2=2)
print(output)


# ### Call the function using positional arguments

# In[7]:


output = add_two_numbers(-1, 4)
print(output)


# ## Positional vs. Keyword Arguments...be careful!
# * If you have multiple input arguments and you pass by position, then you have to get the order of the arguments correct...otherwise unexpected errors can happen (and they might not explicitly throw an error, so they can be hard to spot!)
# * Thus, if you have multiple input arguments it is good practice to pass by keyword instead of position
# * When passing by keyword, the order doesn't matter, so long as you have the correct keywords

# In[8]:


def exp(num, exponent):
    return num ** exponent


# ### Call by positional arguments: 2**3, so expected output is 8

# In[9]:


exp(2, 3)


# ### Call by keyword arguments: expected value is 8

# In[10]:


exp(num=2, exponent=3)


# ### Call by positional arguments: expected value is 8 but suppose you forgot that num comes first and exponent comes second...expected result is still 8 but you get 9 instead (i.e. 3**2 = 9)

# In[11]:


exp(3, 2)


# ### So even though its bad practice to flip the order of parameters, passing by keyword will save you and produce the expected result

# In[12]:


exp(exponent=3, num=2)


# ### Note: once you have a keyword argument, you can't have other positional arguments afterwards

# In[13]:


exp(num=2, 3)


# ## Setting a default value for parameters
# * You sometimes want to set a default value for a parameter...this is allowed during function **definition**

# In[14]:


def exp(num, exponent=2):
    return num ** exponent


# ## Multiple operations in a single function
# * We aren't limited to a single operation within a function. 
# * Instead, we can use multiple operations and all of the concepts we've used previously (including loops and conditionals).

# In[15]:


# determine if a value is even or odd
def even_odd(value):
    if (value % 2 == 0):
        out = "even"
    else:
        out = "odd"

    return out


# In[16]:


# Execute our function
even_odd(-1)


# With functions, the logic behind our code no longer requires it to be executed from top to bottom of the notebook.
# 
# The cost of potential confusion is *definitely* offset by the benefits of writing functions and using modular code.

# ## Function Properties

# - Functions are defined using `def` followed by `:`, which opens a code-block that comprises the function
#     - Running code with a `def` block *defines* the function (but does not *execute* it)

# - Functions are *executed* using parentheses - `()`
#     - This is when the code inside a function is actually run

# - Inside a function, there is code that performs operations on the available variables

# - Functions use the special operator `return` to exit the function, passing out any specified variables

# - When you use a function, you can assign the output (whatever is `return`ed) to a variable

# ## Global and local namespaces
# * Functions have their own namespace, called the **local namespace**, and they only have access to variables explicitly passed into them
#     * If a variable is declared or assigned inside of function, that variable only exists during the executation of the function.
#     * These local variables are not visible or usable outside of the function
# * In contrast, variables declared outside of a function are in the **global namespace**. This is what we've been doing thus far in the course, and global variables are accessible from anywhere in your notebook    
#  
# 

# In[17]:


# Remember, you can check defined variables with `%whos`
get_ipython().run_line_magic('whos', '')


# ### Names defined inside a function only exist within the function
# * In this example, we're using a function that has a **local** variable `x`

# In[18]:


# write a function that subtracts two numbers
def sub(num1, num2):
    
    # assign the difference to the variable x
    x = num1 - num2
    
    # return x
    return x


# ### Now let's define a variable `x` in a normal code cell
# * Since `x` is defined outside of a fucntion, it is a **global** variable that can be seen or accessed from any other regular code cell in our notebook
# * **Important** Even though we are using a variable `x` in our function, it will not overwrite or change the value of the global variable `x` because the local variable `x` only exists within the function

# In[19]:


# assign two integers - these are def
x = 10
y = 17

# pass them into out 'sub' function
d = sub(x, y)

# d will be assigned the difference between x and y
print(f'Output of the function is: {d}')

# Note that when we print the value of our 
# global variable x it is unchanged even though 
# we also used a variable named x in our function
print(f'Global variable x is unchanged: {x}')


# ## Variable number of positional arguments
# 
# You can specify a *variable* number of positional arguments to a function with the special `*` prefix:
# 
# the function definition `def func(a, b, *args)` will assign the first (positional) argument to a, the second to b, and all the rest will be elements of the tuple `args`.
# 

# In[20]:


def myfunction(a, b, *args):
    print('a', a)
    print('b', b)
    print('vars', args)

myfunction(1, 2)

myfunction(1, 2, 'something else')

myfunction(1, 2, 3, 4, 'five!')


# ## More useful examples using *args
# * square all elements of a set of numbers... 

# In[21]:


def squ_nums(*args):
    out = []
    for i in args:
        out.append(i**2)
        
    return out


# In[22]:


print(squ_nums(9,10,12))


# ### Find the max value of a set of numbers

# In[23]:


def my_max(*args):
    
    # check to make sure all elements are numbers
    # if there are non-numerical values (like a string)
    # then return a message to user letting them know
    for i in args:
        if not isinstance(i, int) and not isinstance(i, float):
            return 'non numerical input'
    
    # start by assigning first input 
    # value to a variable that stores the 
    # max (m)
    m = args[0]
    
    # then loop over all the remaining
    # elements
    for i in args[1:]:
        # if the current element is 
        # bigger than the previous max
        # then reassign
        
        if i > m: 
            m = i
            
    return m


# In[24]:


my_max(0,7,100,2.0)


# In[25]:


my_max(0,7,100,'2.0')


# ## Variable number of keyword arguments
# * You can specify a *variable* number of keyword arguments to a function with the special `**` prefix:
# * The function definition `def func(a, b, **kwargs)` will assign the first (positional) argument to a, the second to b, and all the rest will be elements of the dictionary `kwargs`.
# * **Important**: You need to the keyword argument notation that we covered above (e.g. variable_name = value)

# In[26]:


def myfunction(a, b, **kwargs):
    print('a', a)
    print('b', b)
    print('kwargs', kwargs)

# omitting the kwargs are ok...
myfunction(1, 2)

# here is a version with two positional 
# arguments and three keyword arguments 

myfunction(1, 2, x=4, y=5, z=6)

# but notice that **kwargs does not capture positional arguments!
# you have to assign by keyword
myfunction(1, 2, 3)


# ### Note that this definition captures all the positional arguments first, then captures the remaining keyword arguments.  For this reason there may be no positional arguments after a keyword argument.

# In[27]:


myfunction(1, 2, 3, x=4, y=5, z=6, 7)


# ## A more useful example of **kwargs
# * Imagine you run a bike shop or some other store.
# * You want to collect as much information as possible about each customer, but some people don't share much and others share a lot of stuff...
# * Pass all of the user input into a function that creates a dictionary with all provided information. 
# * If you use **kwargs** then you can flexibly accomodate different amounts of info about each user. 
# * Also introduce **docstrings** where you can write helper info about your function so that others can quickly figure out what the function does, what kinds of input you're expecting, and what the function returns. 

# In[28]:


def define_user(name, **info):
    """Accept user input for database

    input: 
    
        name - first name of user
        **info - kwargs...other relevant info in form of key:value pairs

    returns:
    
        dictionary with user info
    """

    # init a blank dictionary
    user_info = {}

    user_info['name'] = name

    # then loop over kwargs
    for k, v in info.items():
        user_info[k] = v

    return user_info


# In[29]:


# see the docstring so we know how to use the function
# define_user?


# In[30]:


usr_info = define_user('john', bike='aethos', car='tacoma', address='24895 Long Valley Rd')
usr_info


# ## Example of abstracting a common operation into a function
# * Recall last week we wrote some code to find a string of text in a book and then we kept N lines of text following the target string
# * Using functions, we can write a general purpose block of code that will take a target string and the number of lines to keep as input parameters. Now we can apply this function to any book and it will do this job for us. 

# In[31]:


def find_str(book,search_target,keep_lines):

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

    return book


# ### Now we can call the function...
# * And the key thing here is that this should work for **any** book or list object with strings of text as elements...i.e. it is now a general purpose function and we don't have to type that code again!

# In[32]:


# open our file for reading...
with open('frankenstein.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    # we'll call the list 'book'
    book = f.readlines()
    
# now call the function...
book_trimmed = find_str(book, 'It was on a dreary night', 10)

print(book_trimmed)


# 
# ## Functions: Review
# 
# 1. `def` defines a function
# 2. `function_name()` - parentheses are required to execute a function
# 3. `function_name(input1)` - input parameters are specified within the function parentheses
# 4. `function_name(input1, input2)` - functions can take multiple parameters as inputs
#     - `input1` and `input2` can then be used within your function when it executes
# 5. To store the output from a function, you'll need a `return` statement
# 6. Local variables exist only within the scope of a function and cannot be accessed outside of the function
# 7. Global variables exist outside the scope of a function and can be seen in all code cells in the notebook
# 8. A variable number of positional or keyword arguments can be passed using the `*` and `**` syntax

# ## More advanced stuff - not covered in class but useful to read

# ### The catch-all function
# * Because you can pass in a variable number of parameters by position (`*`) or by keyword (`**`) you **could** write a function that would take just about anything as input (see below)
# * But please don't do this - it will drive people crazy because they won't know what kind of input the function expects, and it is almost always better to have well defined functions with a specific *signature*.

# In[33]:


def myfunction(*args, **kwargs):
    print('args', args)
    print('kwargs',kwargs)


print('\nmyfunction()')
myfunction()

print('\nmyfunction(1, 2, x=4, y=5, z=6)')
myfunction(1, 2, x=4, y=5, z=6)

print('\nmyfunction(1, 2, 3)')
myfunction(1, 2, 3)

print('\nmyfunction(1, 2, 3, x=4, y=5, z=6)')
myfunction(1, 2, 3, x=4, y=5, z=6)


# ### Calling functions within other functions
# * Suppose we wrote a function called `is_odd()` which takes an input `value`,

# In[34]:


def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False

    return answer


# To use the function, we can execute `is_odd(value)`

# In[35]:


out = is_odd(6)
out


# Later on, if you wanted to use that function _within another function_ you still have to pass an input to the function.

# In[36]:


def new_function(my_list):
    output = []
    for val in my_list:
        # here we can call our other function `is_odd`
        if is_odd(val):
            output.append('yay!')
    return output


# In[37]:


new_function([1,2,3,4])


# ### Note about function signatures and type annotation
# 
# Although it is possible to define all functions as a catchall function: `def f(*args, **kwargs):` that would be terrible in practice, because then it is nearly impossible to figure out what kind of input the function expects.  Consequently you ought to define functions in the most restrictive manner possible.  If you expect one argument, define the function accordingly.
# 
# In Python you can also add type **annotations** to your function definitions.  These are not used directly by the python interpreter, but are often used by the IDE to help you write code.  This is also good practice as it makes it clear what kind of arguments your function expects and returns.
# 

# In[38]:


def transformString(string: str) -> str:
    return string.lower()


# ### More formal explanation of local/global namespaces 
# * Variables in python are passed to functions by *assignment*.
# * Recall that we can assign two names to the same object:

# In[39]:


a = 'hello'
b = a         # b takes on the value of a

# since they are both referring to the same 
# value ('hello') they have the same id...
# we can also say that they b is a `view` of a...
print(id(a))
print(id(b))


# when we pass something to a function, we are effectively assigning a new (local) name to that same object.

# In[40]:


def func(x):
    print(id(x))
a = "hello"
print(id(a))
func(a)


# This is nice, because we don't have to allocate more memory to store a *copy* of that object when we pass it into a function.  However, weird things might happen, depending on what we do to that object.
# 

# In[41]:


def func(x):
    print('enter function')
    print('    x:', x)
    print('    id(x)', id(x))
    x = 'boo'
    print('    x:', x)
    print('    id(x)', id(x))
    print('exit function')

a = "hello"
print('a:', a)
print('id of a globally', id(a))
func(a)
print('a:', a)
print('id of a globally', id(a))


# * So what happened here is that `x` inside the function started off pointing to the same object as `a` globally, but then, when we reassigned a new string to `x`, these two variables pointed to different objects, and the local changes to `x` did not alter the object referred to by the global name `a`.
# 
# * This happens because we *reasigned* a value to `x`.  
# 
# * However, some objects we can alter in place, and as a consequence, local changes will also carry over to the global variable.

# In[42]:


def func(x):
    print('enter function')
    print('    x:', x)
    print('    id(x)', id(x))
    x.append('boo')
    print('    x:', x)
    print('    id(x)', id(x))
    print('exit function')

a = ["hello"]
print('a:', a)
print('id of a globally', id(a))
func(a)
print('a:', a)
print('id of a globally', id(a))


# Here, we used a list variable, which is *mutable*, and we called a method of that object that mutates that variable in place.  The consequence is that we changed the object, that the global and local variables pointed to, and the changes we made inside the function persisted outside the function.
# 
# If we instead changed the variable inside the function via reassignment, then those changes would stay local.  (This is a case in which `x += [a]` behaves differently from `x = x + [a]` because the `+=` operator uses an inplace method to append).

# In[43]:


def func(x):
    print('enter function')
    print('    x:', x)
    print('    id(x)', id(x))
    x = x + ['boo']
    print('    x:', x)
    print('    id(x)', id(x))
    print('exit function')

a = ["hello"]
print('a:', a)
print('id of a globally', id(a))
func(a)
print('a:', a)
print('id of a globally', id(a))

