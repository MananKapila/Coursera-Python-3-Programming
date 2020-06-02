# Python provides a statement called 'assert'.
#       -> Following the word assert there will be a python expression.
#       -> If that expression evaluates to the Boolean False, then the interpreter will raise a runtime error.
#       -> If the expression evaluates to True, then nothing happens and the execution goes on to the next line of code.
a = 1
b = 1
assert a == b  # prints nothing, meaning that the assertion passed
b = 2
assert a == b  # runtime AssertionError

# Why doesn't 'assert' print out something saying that the test passed? The reason is that you don’t want to clutter up
# your output window with the results of automated tests that pass. You just want to know when one of your tests fails.
# In larger projects, other testing harnesses are used instead of 'assert', such as the python 'unittest' module.

# Generally, we should test the behaviour of a function both by omitting and providing various values for its optional
# parameters.
assert sorted([1, 2, 3], reverse=True) == [3, 2, 1]  # prints nothing, meaning that the assertion passed
assert sorted([1, 2, 3], reverse=False) == [3, 2, 1]  # runtime AssertionError
assert sorted([1, 2, 3]) == [3, 2, 1]  # runtime AssertionError

# Tip: it is always a good idea to write tests first, and then start developing the functionality!
# (google 'Test-driven development cycle')

