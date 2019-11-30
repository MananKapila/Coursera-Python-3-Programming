# An alternative notation for creating a function is the lambda expression.
# The syntax of a lambda expression is the word “lambda” followed by parameter names, separated by commas but not
# inside (parentheses), followed by a colon and then an expression.
# lambda arguments: expression
# The statement above yields a function object. This unnamed object behaves just like the function object constructed
# below:
# def f(arguments):
#    return expression

# For example, this lambda expression:
lambda x: x + 1


# is equivalent to the following function definition:
def f(x):
    return x + 1


# We can check that the lambda expression is essentially a function by verifying its type.
print(lambda x: x + 1)  # <function <lambda> at 0x00000266209EC9D0>
print(type(lambda x: x + 1))  # <class 'function'>

# We can call an anonymous lambda functions like this:
(lambda x: x + 1)(5)
print((lambda x: x + 1)(5))  # 6

# Instead of using lambda expressions as anonymous functions, we can also give them names.
lf = lambda x: x + 1

# Let's do a comparison between our classically-defined function (f) and our function defined through the equivalent
# lambda expression (lf).
print(f)  # <function f at 0x00000215D019C9D0>
print(type(f))  # <class 'function'>
print(f(1))  # 2

print(lf)  # <function <lambda> at 0x00000215D019CA60>
print(type(lf))  # <class 'function'>
print(lf(1))  # 2
# We can see that the two are essentially the same.

# An important observation is that Python does not allow multi-line lambda expressions, because they would clash,
# syntactically, with the other syntax constructs in Python.
