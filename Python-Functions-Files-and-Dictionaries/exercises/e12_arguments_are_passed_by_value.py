# We may have already noticed that, much like Java, Python uses primitives (built-in types) and references to objects.
# The primitive (built-in-types) in Python are integers, floats, booleans and strings.

# The semantics of assigning and passing arguments are exactly the same in Python as in Java.
# Both Java and Python are described as being pass-by-value. That is, the argument passed to a function is duplicated so
# that the function will work on a copy of it.
# Confusion arises because that argument might sometimes be a reference to an object. We must keep in mind that the
# reference is the one being duplicated (thus, obtaining an alias for the reference sent as parameter), not the object
# itself!

# We most clearly see the effect of pass-by-value in this simple example:
def double(y):
    y = 2 * y
    print(y)


y = 5
double(y)  # 10
print(y)  # 5


# The double function works on its own copy of the y primitive.


# The following is an example of passing a REFERENCE by value (and a case where confusion might arise):
def change_it(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
    print(lst)


mylst = ['our', 'students', 'are', 'awesome']
change_it(mylst)  # ['Michigan', 'Wolverines', 'are', 'awesome']
print(mylst)  # ['Michigan', 'Wolverines', 'are', 'awesome']
# The change_it function operated on a physical copy of the mylst reference, not of the list to which mylst points to!
# Both mylst and its alias passed to change_it refer to the same list in memory!

# Cases such as the latter cause side-effects to appear when passing parameters to functions.
# In general, any lasting effect that occurs in a function, not through its return value, is called a side effect.
# There are three ways to have side effects:
#       - Printing out a value. This does not change any objects or variable bindings, but it does have a potential
#       lasting effect outside the function execution, because a person might see the output and be influenced by it.
#       - Changing the value of a mutable object.
#       - Changing the binding of a global variable.

# Side effects are sometimes convenient. For example, it may be convenient to have a single dictionary that accumulates
# information, and pass it around to various functions that might add to it or modify it.
# However, programs that have side effects can be very difficult to debug. When an object has a value that is not what
# you expected, it can be difficult to track down exactly where in the code it was set.
# Wherever it is practical to do so, IT IS BEST TO AVOID SIDE EFFECTS!
# The way to avoid using side effects is to use return values instead.

# If functions never ever have side effects, that's a style called functional programming. There are programming
# languages built around that principle of functional programming but Python is more flexible, and we will sometimes
# make use of side effects but you should do it sparingly and consciously.
# Because it's preferable to avoid function side-effects, it is best to come as close to strict functional programming
# as we can.
