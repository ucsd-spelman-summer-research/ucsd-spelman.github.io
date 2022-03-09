#!/usr/bin/env python
# coding: utf-8

# # P01:  Python syntax, variables, types
# 
# ## Python Syntax
# 
# Python is a programming language.  Unlike human languages, programming languages have a very strict syntax.  One virtue of this is that code written in a programming language is unambiguous -- there is only one way that Python can interpret that code.  The downside is that our intuitions from speaking human language can make it difficult to comply with a very strict syntax, semantics, vocabulary, etc. This is perhaps the hardest concept to learn when programming, but you will  get used to it with practice!

# ### Comments
# 

# In[1]:


# a line of code starting with the # character is a comment.
# The python interpreter ignores it.
# Consequently, this code cell does nothing.


# ### Expressions
# 
# Anything in a block of code that is not a comment, Python reads from top to bottom, and treats as an **expression**.  Python tries to parse it (into sub-expressions), and then tries to **evaluate** those expressions.
# 
# As an example

# In[2]:


x = 34
print(x)


# Python reads the `x = 34` line first.  It parses this into a binary operator expression: `exp op exp` with the assignment operator:  `exp_1 = exp_2`. The left hand expression is the name `x`, and the right hand expression is the literal `34`.  Python evaluates the literal `34` which returns the integer 34; that value is then assigned to the variable named `x`.
# 
# The next line is parsed as a call expression.  The `print()` function is called on a sub-expression.  That sub-expression contains the name `x`.  Python evaluates `x` to obtain the integer 34.  And that is passed to the print() function.  The print function calls a particular method in the integer object to obtain its string representation, and then prints that representation.
# 
# This is all a bit fast and loose, but the parts that are worth remembering:
# - Python has to parse the code you type and if your code is ambiguous or does not conform to the python syntax, then you will get an error!

# ### Literals
# 
# Some kinds of things that we can type into the Python interepreter are interpreted literally.  For instance, a number is interpreted as a number literal, and some characters inside quotes are interpreted as a string literal, the word True (and False) are interpreted as Boolean literals.

# In[3]:


34


# In[4]:


'abc'


# In[5]:


True


# ### Names
# 
# Without quotes, `abc` is interpreted by Python to be a reference to an object in memory (i.e., a variable).  When no object in memory has such a name, we get a `NameError`.

# In[6]:


abc


# ### Errors and Exceptions
# 
# As you write code, you will encounter problems of various sorts: syntax error and exceptions.
# 
# Problems of these sorts mean that the Python interpreter cannot do what you have
# told it to do.  There are many different kinds of exceptions you will encounter, and the specific type of exception tells you something about what is wrong with your code.
# 
# A **SyntaxError** (or **IndentationError**): means that Python does not know how to parse the instructions you wrote, and cannot even begin executing them.
# 
# Other kinds of errors arise while the program is executing (during *runtime*).  Such runtime **Exceptions** mean that Python cannot do what you have asked of it.
# 
# For a bit more on fixing errors see [debugging](../course/debugging.md)

# In[7]:


3 +


# In[8]:


abc


# In[9]:


'3' + 4


# Note that for strings, the quotes have to be closed, and must match.  `'abc'` is an acceptable string literal.  `"abc"` is also an acceptable string literal.  `'abc"`, `"abc'`, `'abc`, `"abc` are all syntax errors because Python cannot figure out where the string started by the first quote is supposed to end:

# In[10]:


'abc'


# In[11]:


"abc"


# In[12]:


'abc"


# In[13]:


"abc'


# In[14]:


'abc


# In[15]:


"abc


# ### sometimes you need to mix and match ' with " if you want quotes or apostrophes in your string...

# In[16]:


I don't want to do my homework'


# In[17]:


"I don't want to do my homework"


# ### functions
# 
# We will talk much more about functions when we start writing them ourselves, but for now, we just need to know that functions are stored procedures, which we can call by invoking their name, and passing some arguments to them:  `functionname(argument)`.
# 
# For instance, the `print()` function prints whatever you give it.

# In[18]:


print('hello!')
print('with the print function, we can print many lines in one cell!')


# ### White space
# 
# Python treats white space (i.e., spaces, tabs, etc.) as meaningful.  Some puzzling syntax errors might arise from improperly indenting code.

# In[19]:


print('hello')
   print('with the print function...')


# Other syntax errors might arise from mixing spaces and tabs.  We will talk more about indenting in the context of code blocks.  For now, just be aware that even though blank spaces just look like space to you, they are a meaningful character to the python interpreter.  It might make sense if you visualize what the interpreter sees -- the white space is shown to us as a blank, but the computer encodes it with characters, like any other character.
# 
# `
# print('hello')
# ␣␣␣print('with the print function...')
# `

# ## Python types
# 
# Computer programs do stuff to data.  The data has to somehow be represented in the computer.  Ultimately, all the data is represented in binary in computer memory, but we generally don't have to deal with the binary ourselves, we deal with more abstracted data representations.  However, Python needs to know what kind of data it is dealing with, to determine what to do with the relevant binary information.  Thus, data are encoded in some kind of data type, and the *data type* is of utmost importance to how Python will interpret our commands.  There are many different types of data and data structures in Python.  Today we will deal with the basics: integers, floating point numbers, strings, and boolean values.
# 
# The important thing to remember is that how things *appear* is different from how things are **represented** in the computer.  So when investigating what Python might do to a certain variable, we must know not only the value of the variable, but also its **type**.
# 
# ### type()
# 
# the `type()` function takes some argument, and returns the data type of the object referenced by that argument.  If we pass in a literal, it will tell us the literal's type.

# In[20]:


type('34')


# In[21]:


type(34.0)


# In[22]:


type(34)


# In[23]:


type(True)


# The basic data types we have encountered so far are
# - `str`: strings, which are sequences of characters -- text. (more in a bit)
# - `int`: integers, which are whole (integer) numbers.
# - `float`: floating point numbers, which are numbers that have decimals.
# - `bool`: boolean / binary values, used for all logical operations: either `True`, or `False`.
# 
# 
# ### Looks can be deceiving
# 
# Variable contents that look similar to the human eye may be treated very differently by the computer.  Let's not worry about all these particular types just yet, just remember that the *type* of a variable is of utmost importance to a computer, but is not intuitively relevant to most people.

# In[24]:


a = '345'
b = 345
c = 345.0
d = (345,)
e = [345]
f = {'#':345}
g = None
h = 'None'
i = True
j = 'True'


# #### isinstance()
# 
# We can check if a given variable is a certain type with the isinstance() function

# In[25]:


x = 34
isinstance(x, int) # True
isinstance(x, float) # False
isinstance(x, str) # False


# ## Python Operators
# 
# Operators are special symbols that take some arguments, do something to them, and return some value.  The basic binary (meaning they take two values) arithmetic operators are very familiar, when applied to numbers:

# In[26]:


3 + 4


# In[27]:


3 - 4


# In[28]:


3 * 4


# In[29]:


3 / 4


# In[30]:


3 ** 4


# Note, that last one might be a bit surprising.  the `**` operator corresponds to exponentiation, so `3 ** 4` calculates $3^4$ (i.e., $3 * 3 * 3 *3$)

# In[31]:


11 % 7


# this modulus operator may be surprising -- it returns the *remainder*.  11 / 7 is 1 with a remainder of 4.  so 11 % 7 returns 4.
# * A very handy use of the modulus operator is to determine if a number is even or odd...if it is even then the number modulus 2 is 0, otherwise the number is odd!

# In[32]:


4 % 2


# In[33]:


7 % 2


# ### Operator precedence
# 
# As in basic arithmetic, operators have precedence: some of them are executed first, and parentheses can be used to group operations to set a precedence order.
# * Remember PEMDAS (paren, exp, multiply, divide, add, sub)

# In[34]:


14 - 3 * 2


# In[35]:


(14 - 3) * 2


# ### Operators and types
# 
# As we saw, a given literal has a type, and what it means to apply a given operation to a particular entity depends on its type.
# 
# For instance, some operations don't make any sense for certain types:

# In[36]:


'css ' * 'class'


# The cell above yields a `TypeError` because Python does not have a defined operation corresponding to `*` for two strings.  That makes sense -- after all, what do you think such an operation could mean?
# 
# Some confusion may arise because, sometimes, the operation might look meaningful to us, but not to Python, because Python does not interpret code the same way we do.  For instance `'3' * '4'` makes sense to us, but not to Python.  The reason is that to Python `'3'` and `'4'` are strings, the fact that those strings *could* be interpreted as numbers is irrelevant for Python until we explicitly ask it to interpret those strings as integers.  At the level of data types, `'3'` and `'4'` are no different from a string like `'css'`.  All it knows is that you have asked it to apply `*` to two strings, and it does not think that is a valid operation.

# In[37]:


'3' * '4'


# ### Type casting
# 
# When *we* see `'3' * '4'` we are implicitly converting ("casting") the strings into integers.  We need to do so explicitly for python to understand.  Which we can do with the `int()` function.

# In[38]:


int('3') * int('4')


# Of course, some strings cannot be converted to integers, what would it even mean?

# In[39]:


int('css')


# Some types of conversion might make sense to us, but Python does not understand them:

# In[40]:


int('three')


# In short, if we are trying to convert a string to an `int` (or a `float`), then the string ought to be interpretable as an integer or a float if we were to just provide it to Python directly, as a literal, without quotes.  Otherwise, Python will not know how to convert it, and will throw a `ValueError` exception

# ### Overloaded operators
# 
# Many operators can work for different types, but they do different things depending on what the types are.  For instance consider `+`:
# - `int + int -> int`: for two integers, `+` takes their sum, and returns it as an integer.
# - `float + float -> float`: for two floating point numbers, `+` takes their sum and returns another floating point number.
# - `float + int -> float`: for a floating point number and an integer, `+` takes their sum and returns a floating point number.
# 
# These are mostly obvious: `+` applied to two numbers returns their sum.  Slightly less obvious is what number data type it returns: for two integers it returns another integer, but if a float is involved, it will return a float.

# In[41]:


3 + 3


# In[42]:


3.0 + 3.0


# In[43]:


3 + 3.0


# Less intuitively, `+` can also be applied to two strings:
# 
# - `str + str -> str`: when applied to two strings, `+` returns the concatenation of the two strings.

# In[44]:


'3' + '3'


# Some combinations of types, however, do not work with `+`:  `str + int` will return a TypeError.

# In[45]:


'3' + 3


# Another, common and surprising operator type combination that works:
# 
# - `str * int -> str`: a string `*` an integer `n` returns that string, repeated `n` times.  (this also works for other sequences, which we will see later)
# 
# This has a certain logic to it: if we think of multiplication as repeated addition, and addition of strings is concatenation, then multiplication of strings would be repeated concatenation.

# In[46]:


'a' * 5


# In[47]:


2 * 'hip ' + 'hooray'


# In[48]:


'a' * 5.0


# (note that this works for *integers* not *floats*.  Even if the float is a round number.
# 
# The combination of type casting, and operator overloading yields some potentially puzzling behavior.
# 
# consider what the lines below will return:
# - `str(3) + str(4)`
# - `str(3) + 4`
# - `int('3') * 4`
# - `int('3') * str(4)`
# etc.

# ## Python: variables, execution
# 
# ### Variables
# 
# We will need to store things in memory.  To do so, we will use variables.  A variable is a name that we can assign to an object, and refer to that object later.  We use the assignment operator `=` to do this.
# 
# > **Note that this is *assignment* not mathematical *equality*.**
# >
# > **Mathematical equality** is a declarative statement of fact.  $x = 4y+3$ declares a particular fact: that a certain relationship holds.  We can do algebra to derive other facts from this one (e.g., $x-3 = 4y$ and $y=x/4 - 3/4$).  So a statement like $x = x + 1$ is invalid because from it we can derive a contradiction, such as $0 = 1$.
# >
# > **Assignment** is a procedural instruction, where we tell the computer to evaluate the stuff on the right hand side, and assign the output to the left hand side.  So a statement like `x = x+1` is totally fine.  We calculate `x+1` on the right hand side, then assign that value to `x`.  The net effect is that we have incremented the value of `x` by 1.
# 

# In[49]:


greeting = 'Hello!  This is a long string describing how we greet you!'

print(greeting)


# By assigning values to variables, we can use them many times.

# In[50]:


radius = 4
pi = 3.14159

print('area: ', pi * radius ** 2)
print('circumference: ', 2 * pi * radius)


# ### Sequential execution
# 
# Within a given code block, instructions are executed in a particular sequence, and future instructions (such as changing the value of a variable) do not change the calculations (and assignments) from prior instructions:

# In[51]:


a = 3
b = 4
x = a * b
a = 5
print('x: ', x)
print('a*b: ', a*b)


# ## Reading code
# 
# When **reading** code, it is important that you consider not just what the lines are telling the computer to do, but what the *state* of the program in memory is at the moment that the computer follows those instructions.
# 
# For instance, to think through what the code above is doing, let's step through it.  Starting with the memory state before the first line is even evaluated.
# 
# > *memory state:* `{}` (blank, other than built in stuff)
# 
# `a = 3`: assign value 3 to variable named `a`
# 
# > *memory state:* `{'a': 3}`
# 
# `b = 4`: assign value 4 to variable named `b`
# 
# > *memory state:* `{'a':3, 'b':4}`
# 
# `x = a * b`: `a` evaluated to `3` (`x = 3 * b`), `b` evaluated to `4` (`x = 3 * 4`), `*` applied to `3` and `4` to yield `12` (`x = 12`), `12` is assigned to `x`.
# 
# > *memory state:* `{'a':3, 'b':4, 'x':12}`
# 
# `a = 5`: assign value 5 to variable named `a`
# 
# > *memory state:* `{'a':5, 'b':4, 'x':12}`
# 
# `print(x)`: `x` evaluated to `12` (`print(12)`), `print()` prints `12`
# 
# > *memory state:* `{'a':5, 'b':4, 'x':12}`
# 
# `print(a*b)`: `a` evaluated to `5` (`print(5*b)`), `b` evaluated to `4` (`print(5*4)`), `*` applied to `5` and `4` to yield `20` (`print(20)`), `print()` prints `20`
# 
# > *memory state:* `{'a':5, 'b':4, 'x':12}`
# 
# When dealing with more complicated programs and algorithms, it is sometimes very helpful to do this with paper and pencil, to make sure you can think through what each line is doing to the memory state. Alternatively you can (1) insert print statements to check specific variable values (print [debugging](https://en.wikipedia.org/wiki/Debugging)), (2) in jupyter notebooks, insert IPython `%whos` linemagic to check all variables in memory, or (3) run the code in [python tutor](http://pythontutor.com/).
# 
# Below I demonstrate the second method:

# In[52]:


# this line clears all prior variables from memory
get_ipython().run_line_magic('reset', '-f')

# shows contents of variables in memory
get_ipython().run_line_magic('whos', '')
print('') # prints an empty line for easier reading.

a = 3
get_ipython().run_line_magic('whos', '')
print('')

b = 4
get_ipython().run_line_magic('whos', '')
print('')

x = a * b
get_ipython().run_line_magic('whos', '')
print('')

a = 5
get_ipython().run_line_magic('whos', '')
print('')

print('x: ', x)
print('a*b: ', a*b)


# ### Notebooks, cells, and memory state.
# 
# Important Note: This kind of logic for stepping through code works great when considering stand alone scripts.  Notebooks, however, are pretty tricky, because each cell runs code in the same environment, so the memory state at the start of the cell is determined by which cells had been run previously.  (this is why I used `%reset -f` above, to clear all variables from prior cells).

# In[53]:


# note that x is still in memory, even though it was not defined in this cell!
print(x)


# Cells *could* be run out of order.  This presents a great deal of opportunity for confusion.   Make sure that you can run your whole notebook from start to finish, in the order it is written!
# 
# In jupyter notebooks, you can use the 'line magic' commands `%who` to see a list of currently declared variables in memory, and `%whos` to also see their values.

# In[54]:


get_ipython().run_line_magic('who', '')


# In[55]:


get_ipython().run_line_magic('whos', '')


# ### Print debugging

# In[56]:


a = input('enter number a: ')
b = input('enter number b: ')
print(a+b)


# The most generic (and arguably most powerful) way to figure out why a program is not doing what you want it to do (i.e., to "debug" a program) is to insert `print()` statements into the code, to ask the program to print out the current values (and types!) of various variables in memory.  Often this will reveal that variables do not have the values you expected, and you can figure out at what point in the program your expectations diverge from what the code is actually doing.

# In[57]:


a = input('enter number a: ')
b = input('enter number b: ')
print(type(a), a)
print(type(b), b)
print(a+b)

