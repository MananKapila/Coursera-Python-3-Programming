# In the previous section, on Optional Parameters you learned how to define default values for formal parameters, which
# made it optional to provide values for those parameters when invoking the functions.

# In this chapter, you’ll see one more way to invoke functions with optional parameters, with keyword-based argument
# passing. This is particularly convenient when there are several optional parameters and you want to provide a value
# for one of the later parameters while not providing a value for the earlier ones.

# Let's review the following example, where we have two consecutive optional parameters:

def f(x, y=3, z="hi"):
    print("x = {} , y = {} , z = {} ".format(x, y, z))


# We send a value for the x parameter.
f(1)  # x = 1 , y = 3 , z = hi
# We send values for the x and y parameters.
f(1, 2)  # x = 1 , y = 2 , z = hi
# We send values for the x, y and z parameters.
f(1, 2, 3)  # x = 1 , y = 2 , z = 3

# What if we want to only pass values for the x and z parameters? We'd have to somehow skip y. But how do we do that
# without the function misinterpreting one of our arguments as being meant for y?
# We can't just write f(1, ,3) because python doesn't understand this syntax.

# The solution is: keyword arguments!
# We can specify which parameters we're sending the values for by using the = sign.

# We send values for the x and z parameters.
f(1, z="bye")  # x = 1 , y = 3 , z = bye
# Arguments not accompanied by keywords are called positional arguments (the kind we were already used to).

# We can even use keyword arguments for non-optional parameters!
f(x=1, y=2, z=3)  # x = 1 , y = 2 , z = 3

# However, we must be careful not to specify two values for the same parameter, by either:
# - using the same keyword twice
# f(x=1, x=1, z=3) # IDE warning: Keyword argument repeated,
# - or (a more subtle mistake) sending a positional argument and a keyword argument for the same parameter
# f(1, x=1, z=3)
# In both cases, we would get a runtime error: TypeError: f() got multiple values for argument 'x'

# A nice thing that keyword arguments allow us to do is to mix the order of our arguments in any way we want:
f(z=3, y=2, x=1)  # x = 1 , y = 2 , z = 3

# Keyword arguments must always follow positional arguments.
