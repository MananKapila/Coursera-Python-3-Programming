# We have previously seen tuples, a sequence type that works just like lists except that they are immutable.
# When working with multiple values or multiple variable names, the Python interpreter does some automatic packing and
# unpacking to and from tuples, which allows some simplifications in the code we write.

# ================================================== Tuple packing ====================================================
# Wherever python expects a single value, if multiple expressions are provided, separated by commas, they are
# automatically packed into a tuple. For example, we could have omitted the parentheses when first assigning a tuple
# to the variable julia.
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# or equivalently:
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(type(julia))  # <class 'tuple'>
print(julia[4])  # 2009


# ============================================= Tuples as return values ===============================================
# Functions can return tuples as return values. This is very useful — we often want to know some batsman’s highest and
# lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month, and the
# day, or if we’re doing some ecological modeling we may want to know the number of rabbits and the number of wolves on
# an island at a given time. In each case, a function (which can only return a single value), can create a single tuple
# holding multiple elements.
# For example, we could write a function that returns both the area and the circumference of a circle of radius r.
def circle_info(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)


print(circle_info(10))  # (62.8318, 314.159)


# Again, we can take advantage of packing to make the code look a little more readable on the last line of the function:
def circle_info(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a


# ================================================= Tuple unpacking ====================================================
# Python has a very powerful tuple assignment feature that allows a tuple of variable names on the left of an assignment
# statement to be assigned values from a tuple on the right of the assignment. Another way to think of this is that the
# tuple of values is unpacked into the variable names.
name, surname, birth_year, movie, movie_year, profession, birth_place = julia
# This does the equivalent of seven assignment statements, all on one easy line. One requirement is that the number of
# variables on the left must match the number of elements in the tuple.
print(name)  # Julia
print(surname)  # Roberts
# ...
print(birth_place)  # Atlanta, Georgia
# This powerful tuple assignment comes in handy when we want to swap two variables!
# With conventional assignment statements, we have to use a temporary variable. Tuple assignment solves this problem
# neatly:
a = 1
b = 2
(a, b) = (b, a)
print(a, b)  # 2 1
# Rule: THE LEFT SIDE IS A TUPLE OF VARIABLES. THE RIGHT SIDE IS A TUPLE OF VALUES.
# Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of
# the assignments. This feature makes tuple assignment quite versatile.

# Earlier we were demonstrating how to use tuples as return values when calculating the area and circumference of a
# circle. Here we can unpack the return values after calling the function.
circumference, area = circle_info(10)
print(circumference)  # 62.8318
print(area)  # 314.159


# Python even provides a way to pass a single tuple to a function and have it be unpacked for assignment to the named
# parameters, using the * sign.
def add(x, y):
    return x + y


print(add(3, 4))  # 7
z = (5, 4)
# print(add(z)) # TypeError: add() missing 1 required positional argument: 'y'
# In order to send the tuple as one parameter that will be unpacked by the function, we need to use the * sign:
print(add(*z))  # 9


# We can simultaneously send several tuples as parameters to the same function, to be unpacked.
def add(m, n, o, p):
    return m + n + o + p


r = (1, 2)
s = (3, 4)
print(add(*r, *s))  # 10

# UNPACKING INTO MULTIPLE VARIABLE NAMES ALSO WORKS WITH LISTS, OR ANY OTHER SEQUENCE TYPE, as long as there is exactly
# one value for each variable. For example, you can write:
x, y = [3, 4]
print(x)  # 3
print(y)  # 4

# ======================================== Unpacking into iterator variables ===========================================
# Multiple assignment with unpacking is particularly useful when you iterate through a list of tuples or lists.

# For example, a dictionary consists of key-value pairs. When we call the items() method on a dictionary, we get back a
# sequence of key-value pairs. Each of those pairs is a two-item tuple.
d = {"k1": 3, "k2": 7, "k3": "some other value"}

for dict_pair in d.items():
    print("key: {}, value: {}".format(dict_pair[0], dict_pair[1]))

# Each time the print line is executed, dict_pair will refer to one key-value pair from d. A pair is just a tuple, so
# p[0] refers to the key and p[1] refers to the value.
# That code is easier to read if we unpack the key-value pairs into two variable names:

d = {"k1": 3, "k2": 7, "k3": "some other value"}

for key, value in d.items():
    print("key: {}, value: {}".format(key, value))

# More generally, if we have a list of tuples that each has more than two items, and we iterate through them with a
# for-loop, pulling out information from the tuples, the code will be far more readable if we unpack them into separate
# variable names right after the word "for".
