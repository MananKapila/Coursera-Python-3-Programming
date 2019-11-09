# strings are immutable
s = "hi"
# points s to another location in memory
s = "hello"
# prints hello
print(s)



# lists are mutable sequences (collections in which order matters)
list = [10, 20, 30]
print(list)
# a list can contain elements of various types (even other lists)
list = [10, 20, "hey there", [3, "cool"]]
print(list)



# tuples are immutable sequences
# they differ from lists only in mutability and syntax
# (they use parentheses instead of square brackets)
tuple = (10, 20, "hey there", [3, "cool"])
print(tuple)
# points tuple to another location in memory
tuple = (1,2,3)
# prints (1,2,3)
print(tuple)
# Word of caution:
# If you want to create a tuple with a single element,
# you might be tempted to write something like this:
# tuple = (5) or tuple = ("cats")
# The problem is, python will just treat what we wrote
# as an integer/string/etc in parentheses.
tuple = (5)
# will print 5
print(tuple)
tuple = ("cats")
# will print 'cats'
print(tuple)
# What we need to do, in order to specify to python that
# we want to create a single-element tuple, is to add a
# comma after the elemnt:
tuple = (5,)
# will print (5,)
print(tuple)
tuple = ("cats",)
# will print ('cats',)
print(tuple)
