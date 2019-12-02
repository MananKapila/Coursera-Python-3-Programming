# Sorting dictionaries might be a little more subtle, because now we're talking about a collection of pairs.

d = {3: "third", 2: "the second", 1: "first"}
# We remember that iterating through a dictionary essentially means iterating through its keys:
for k in d:
    print(k)
# 3
# 2
# 1

# In python, when we pass a dictionary to something that is expecting a list, its the same as passing the list of keys.

# What if we try to call sorted() on a dictionary?
sorted(d)
# What will it return?
#   a) a dictionary sorted by its values (x)
#   b) a dictionary sorted by its keys (x)
#   c) a list of its sorted values (x)
#   d) a list of its sorted keys (CORRECT)
# Because sorted() expects a list of some kind, passing the dictionary will mean that we pass the list of its keys.
# Obviously, what comes out of the sorted() function will also be a list, as usual.
print(type(sorted(d)))  # <class 'list'>
# In this case, the list will represent the dictionary's keys in sorted order.
for k in sorted(d):
    print(k)
# 1
# 2
# 3

# We then are free to access the elements in the dictionary in the order of the keys:
for k in sorted(d):
    print("key {} has value {}".format(k, d[k]))
# key 1 has value first
# key 2 has value the second
# key 3 has value third

# But what if we want to parse the dictionary in the order of its values?
# We have to keep in mind that we cannot directly sort or iterate directly through the values of a dictionary. Instead,
# we will have to sort the list of keys in a way that reflects the order of their values.
# This is where the "key" optional parameter comes in handy. Additionally, instead of defining a function, we will use
# an anonymous one through a lambda expression.
# Let's arrange the list of keys in the order of the lengths of their corresponding string values.
for k in sorted(d, key=lambda key: len(d[key])):
    print("key {} has value {}".format(k, d[k]))
# key 3 has value third
# key 1 has value first
# key 2 has value the second
