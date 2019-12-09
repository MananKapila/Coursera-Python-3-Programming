# When constructing our own nested data, it is a good idea to keep the structure consistent across each level.
# For example, if we have a list of dictionaries, then each dictionary should have the same structure, meaning the same
# keys and the same type of value associated with a particular key in all the dictionaries. The reason for this is
# because any deviation in the structure that is used will require extra code to handle those special cases. The more
# the structure deviates, the more you will have to use special cases.

# For example, let’s reconsider this nested iteration, but suppose not all the items in the outer list are lists.
nested1 = [1, 2, ['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
# for x in nested1:
#     print("level1: ")
#      for y in x:
#          print("     level2: {}".format(y))

# The nested iteration above would result in the following error: TypeError: 'int' object is not iterable.
# We can solve this with special casing, a conditional that checks the type.

for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)

# We can imagine how many special case if-thens we’d need, and how complicated the code would get, if we had many
# layers of nesting but not always a consistent structure.

# This is why the lesson we should remember from this exercise is:
# Make data structures very regular, with always the same kinds of items in the same level of nesting. In other words,
# don't mix integers, lists, and dictionaries as items in a single list!

# However, if somebody else puts hazards in our way by mixing types on the same nesting level, we should be prepared to
# handle these situations with "if-then statements"  (one for each different type of data structure).
