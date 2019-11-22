# Variables declared inside a function are local with respect to that function and belong to the function's namespace.
# Variables declared outside any function are global and belong to the global or top-level namespace.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Local variables can never be used globally.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def square(x):
    y = x * x  # y is a local variable
    return y


# Variable y does not exist in the global namespace, so we will get an error if we try to use it without declaring it.
# print(y)  # NameError: name 'y' is not defined

y = 5
# We notice that when we declare y as a global variable, the IDE gives us a warning at the line in our function where
# its local variable y is declared: "Shadows name 'y' from outer scope."
square(2)
# This statement will naturally refer to the global variable y.
print(y)  # 5

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Global variables can sometimes be used locally (practically, only for reads and never for writes).

# <<< If the name of a global variable is assigned a value in a function >>>, the function will create a new, local
# variable with that name, from which it will read and write to, ignoring that global variable.
# <<< Otherwise >>>, the function will just read from the global variable with that name.

# This leads to the conclusion:
# Assignments in a function are always done to local variables!
# Reads in a function are from:
#           - global variables (if variables with the same name are NOT assigned values anywhere inside that function)
#           - local variables (if variables with the same name are assigned values somewhere inside that function)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_var = "i'm global"


def print_message():
    x = 1
    # my_var is not assigned a value in this function, so it will refer the global variable outside the function
    print(my_var)


# The function prints the global variable:
print_message()  # i'm global
print(my_var)  # i'm global


def print_message_2():
    x = 1
    # my_var is assigned a value now, which creates a new, local variable with this name inside the function's namespace
    my_var = "i'm local now"  # Warning: "Shadows name 'y' from outer scope."
    print(my_var)


# The function prints its local variable:
print_message_2()  # i'm local now
# The global variable remains unchanged.
print(my_var)  # i'm global

# ----------> The above rule is the reason why the following function will not return an error:
my_var = 3


def no_error():
    # because my_var is not assigned a value in this function, it's clear that the my_var refers to the global variable
    a = my_var + 1
    b = a + 2


no_error()


# ----------> ...but this one will:
def error():
    # because my_var is later declared in this function, it will treat my_var as a yet-uninitialized local variable
    a = my_var + 1  # Warning: " Unresolved reference 'my_var'"
    my_var = a + 2


# error()  # UnboundLocalError: local variable 'my_var' referenced before assignment

# As we can see, this can be pretty confusing. Therefore, a good, unwritten rule is to:
# NEVER REFER GLOBAL VARIABLES INSIDE FUNCTION DEFINITIONS!
# Even though it is legal in Python, it's not a good idea. Instead, just use parameters, if you want to get outside
# variable inside functions.

# As the Coursera textbook says:
# "It is legal for a function to access a global variable. However, this is considered bad form by nearly all
# programmers and should be avoided.
# This section included some examples that illustrate the potential interactions of global and local variables.
# These help you understand exactly how python works. Hopefully, they also convinced you that things can get pretty
# confusing when you mix local and global variables, and that you really shouldn't do it. "


# Technically, there IS one way of assigning values to global variables in functions.
# It's by using the keyword *global*. However, it is almost never recommended that you do this.
my_var = 1;


def chaning_a_global_variable():
    global my_var
    my_var = 15


print(my_var)  # 1
chaning_a_global_variable()
print(my_var)  # 15

# Generally, MAKING VARIABLES GLOBAL IS CONSIDERED BAD PRACTICE!
