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
