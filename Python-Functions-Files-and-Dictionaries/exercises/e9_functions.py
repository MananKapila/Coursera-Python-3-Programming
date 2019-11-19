# Functions are defined using the *def* keyword. Their content is delimited from the rest of the code by indentation.
def my_function():
    print("hello")
    print("this is our first function in python")


# Functions can include an optional description on the first line, in the form of a string. It's called a doc string.
def my_function_with_doc_string():
    'This is the description of our function'
    print("hello")
    print("this is our first function in python")


# We notice the special style of the doc string in the IDE.
# There are some tools in Python for automatically generating documentation of a program. They will show the docstrings
# that are associated with functions.
# Docstrings are often multi-line, and that's when we use triple quotes.
def my_function_with_multi_line_doc_string():
    """This is the description of our function, but
    it is written
    on multiple
    lines"""
    print("hello")
    print("this is our first function in python")


# This is how we invoke our functions (they all do the same thing):
my_function()
my_function_with_doc_string()
my_function_with_multi_line_doc_string()

# More information on docstrings:
# If the first thing after the function header is a string (some tools insist that it must be a triple-quoted string),
# it is called a docstring and gets special treatment in Python and in some of the programming tools.
# Another way to retrieve this information is to use the interactive interpreter, and enter the expression
# <function_name>.__doc__, which will retrieve the docstring for the function. So the string you write as documentation
# at the start of a function is retrievable by python tools at runtime. This is different from comments in your code,
# which are completely eliminated when the program is parsed.
# By convention, Python programmers use docstrings for the key documentation of their functions.

print(my_function_with_multi_line_doc_string.__doc__)


# This is the description of our function, but
#     it is written
#     on multiple
#     lines

# Functions can receive parameters (sometimes called formal parameters, or input parameters)
def personalized_hello(name):
    print("Hello, {}".format(name))


personalized_hello("Helen")  # Hello, Helen


# Functions can receive one or more parameters (sometimes called formal parameters, or input parameters)
def personalized_hello_multiplied(name, times):
    for i in range(times):
        print("Hello, {}".format(name))


personalized_hello_multiplied("Chuck", 3)


# Hello, Chuck
# Hello, Chuck
# Hello, Chuck

# Functions can also return something.
def square(x):
    y = x * x
    return y


print(square(3))  # 9

# Actually, functions that do not explicitly have a return statement return None.
print(my_function())  # None

# In this example, we want to check wheteher a list contains a name longer than 5 characters.
names = ["Alan", "Jim", "Pat"]


def has_name_longer_than_five_characters(names):
    for name in names:
        if len(name) > 5:
            return True
    return False


print(has_name_longer_than_five_characters(names))  # False
print(has_name_longer_than_five_characters(names + ["Steven"]))  # True


# Because Python is a dynamically typed language, it is always good practice to ask ourselves at least 3 questions, when
# we see a function:
# 1) How many parameters does it take?
# 2) What types are those parameters of?
# 3) What does the function return?
# Because questions 2 and 3 cannot be answered merely by looking at the function's header, we need to do some deductions
# based on the logic inside the function's body.

# Let's take the following example:
def example_function(x, y, z):
    if x - y > 0:
        return y - 2
    else:
        z.append(y)
        return x - 3

# Let's now try to answer the three questions:
# 1) The function takes 3 parameters.
# 2) We see that the function is performing arithmetic operations on x and y. Thereforez we can conclude that x and y
# are numbers - maybe floats or integers. We also notice that we append something to z. We can thus assume that z is a
# list.
# 3) The function returns a number.

# Here are some clues that can help you determine the type of object associated with any variable, including a function
# parameter. If you see…
#
# ----------------------------------------------------------------------------------------------------------------------
#     len(x)        | then x must be a string or a list. (Actually, it can also be a dictionary, in which case it is
#                   | equivalent to the expression len(x.keys()). Later in the course, we will also see some other
#                   | sequence types that it could be). x can’t be a number or a Boolean.
# ----------------------------------------------------------------------------------------------------------------------
#     x - y         | x and y must be numbers (integer or float)
# ----------------------------------------------------------------------------------------------------------------------
#     x + y         | x and y must both be numbers, both be strings, or both be lists
# ----------------------------------------------------------------------------------------------------------------------
#     x[3]          | x must be a string or a list containing at least four items, or x must be a dictionary that
#                   | includes 3 as a key.
# ----------------------------------------------------------------------------------------------------------------------
#     x['3']        | x must be a dictionary, with ‘3’ as a key.
# ----------------------------------------------------------------------------------------------------------------------
#     x[y:z]        | x must be a sequence (string or list), and y and z must be integers
# ----------------------------------------------------------------------------------------------------------------------
#     x and y       | x and y must be Boolean
# ----------------------------------------------------------------------------------------------------------------------
#     for x in y    | y must be a sequence (string or list) or a dictionary (in which case it’s really the dictionary’s
#                   | keys); x must be a character if y is a string; if y is a list, x could be of any type.
# ----------------------------------------------------------------------------------------------------------------------
