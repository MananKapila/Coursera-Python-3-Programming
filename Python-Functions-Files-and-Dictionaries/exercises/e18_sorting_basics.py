# We will introduce two ways in which Python provides out-of-the-box sorting of collections.

# The .sort() method.
# This method sorts a collection by mutating it.
lst = ["i", "have", "great", "news", "for", "you"]
lst.sort()
print(lst)  # ['for', 'great', 'have', 'i', 'news', 'you']
# We notice that the .sort() method does not return anything.
print(lst.sort())  # None

# The sorted() function.
# This function returns a NEW list containing the original one's elements in sorted order. This function does NOT mutate
# the original list.
lst = ["i", "have", "great", "news", "for", "you"]
print(sorted(lst))  # ['for', 'great', 'have', 'i', 'news', 'you']
print(lst)  # ['i', 'have', 'great', 'news', 'for', 'you']
# We notice that for lists of strings, the implicit sorting order is the alphabetical order.

# In general, we will use the sorted() function instead of the .sort() method, because it's safer. We've previously
# emphasized how confusing things can get when we use mutating operations.

# Because strings are also collections, we can sort them too.
s = "Apple"
print(sorted(s))  # ['A', 'e', 'l', 'p', 'p']
# We notice the sorted() function did not return another string, but a list of characters.

# Evidently, we cannot use the .sort() method on strings, as strings are immutable.
# s.sort()  # AttributeError: 'str' object has no attribute 'sort'


l = [1, "hey", 23, "no"]
# An important observation is that Python does not implicitly know how to sort collections containing elements of
# more than one type. For example, trying to sort the list of strings and numbers above with sorted(l) would result
# in the following error: TypeError: '<' not supported between instances of 'str' and 'int'


# The sorted function takes some optional parameters (see e15). The first optional parameter is a key function, which
# will be described in e19. The second optional parameter is a Boolean value which determines whether to sort the items
# in reverse order. By default, it is False, but if you set it to True, the list will be sorted in reverse order.

L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))  # ['Cherry', 'Blueberry', 'Apple']

# This is a situation where it is convenient to use the keyword mechanism for providing optional parameters.
# It is possible to provide the value True for the reverse parameter without naming that parameter, but then we would
# have to provide a value for the second parameter as well, rather than allowing the default parameter value to be used.
# We would have had to write sorted(L2, None, True). That’s a lot harder for humans to read and understand.
