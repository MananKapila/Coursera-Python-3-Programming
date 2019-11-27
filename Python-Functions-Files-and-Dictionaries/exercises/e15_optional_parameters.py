# Formal parameters are usually simply called "parameters". They reside in the function definition.
# Actual parameters are usually called "arguments". They are found in a function call.

# In the treatment of functions so far, each function definition specifies zero or more formal parameters and each
# function invocation provides exactly that many values. Sometimes it is convenient to have optional parameters that
# can be specified or omitted. When an optional parameter is omitted from a function invocation, the formal parameter
# is bound to a default value. When the optional parameter is included, then the formal parameter is bound to the value
# provided. Optional parameters are convenient when a function is almost always used in a simple way, but it’s nice to
# allow it to be used in a more complex way, with non-default values specified for the optional parameters.

# Consider, for example, the int function, which you have used previously. Its first parameter, which is required,
# specifies the object that you wish to convert to an integer. For example, if you call in on a string, int("100"),
# the return value will be the integer 100.
# That’s the most common way programmers want to convert strings to integers. Sometimes, however, they are working with
# numbers in some other “base” rather than base 10. For example, in base 8, the rightmost digit is ones, the next digit
# to the left is 8s, and the one to the left of that is the 64s place (8**2).
# The int function provides an optional parameter for the base. When it is not specified, the number is converted to an
# integer assuming the original number was in base 10. We say that 10 is the default value. So int("100") is the same
# as invoking int("100", 10). We can override the default of 10 by supplying a different value.
print(int("100"))
print(int("100", 10))  # same thing, 10 is the default value for the base
print(int("100", 8))  # now the base is 8, so the result is 1*64 = 64

# When defining a function, you can specify a default value for a parameter. That parameter then becomes an optional
# parameter when the function is called. The way to specify a default value is with an assignment statement inside the
# parameter list.
initial = 7


def f(x, y=3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))


f(2)  # x, y, z, are: 2, 3, 7
f(2, 5)  # x, y, z, are: 2, 5, 7
f(2, 5, 8)  # x, y, z, are: 2, 5, 8
# If you want to provide a non-default value for the third parameter (z), you also need to provide a value for the
# second item (y).
# We will see in the next section a mechanism called keyword parameters that lets you specify a value
# for z without specifying a value for y.

# There are two things to be careful about, when dealing with optional parameters:

# ==================================================== Be careful! ====================================================
# The default value is determined at the time that the function is defined, not at the time that it's invoked.
# =====================================================================================================================
# So in the example above, if we wanted to invoke the function f with a value of 10 for z, we cannot simply set
# initial = 10 right before invoking f.
initial = 10
f(2)  # x, y, z, are: 2, 3, 7


# z still had the value 7 inside the function, because this was its value at the moment the interpreter reached the
# function definition.

# ==================================================== Be careful! ====================================================
#  if the default value is set to a mutable object, such as a list or a dictionary, that object will be shared in all
#  invocations of the function. This can get very confusing, so I suggest that you never set a default value that is a
#  mutable object.
# =====================================================================================================================
# For example, let's see the execution of the following case:
# (We can see that the IDE gives us a warning for the following's function definition:
# "Default argument value is mutable")

def f(a, L=[]):
    L.append(a)
    return L


print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]
print(f(4, ["Hello"]))  # ['Hello', 4]
print(f(5, ["Hello"]))  # ['Hello', 5]


# OPTIONAL PARAMETERS MUST ALWAYS FOLLOW NON-OPTIONAL PARAMETERS!

# Defining this function will result in a runtime error: SyntaxError: non-default argument follows default argument
# def g(x=1, y, z=3):
#     print("x = {} , y = {} , z = {} ".format(x, y, z))
# This does not work either:
# def g(x=1,  z=3, y):
#     print("x = {} , y = {} , z = {} ".format(x, y, z))
# This is the way to go:
def g(x, y=2, z=3):
    print("x = {} , y = {} , z = {} ".format(x, y, z))
