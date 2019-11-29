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

# In general, we will use the sorted() function instead of the .sort() method, because it's safer. We've previously
# emphasized how confusing things can get when we use mutating operations.

# Because strings are also collections, we can sort them too.
s = "Apple"
print(sorted(s))  # ['A', 'e', 'l', 'p', 'p']
# We notice the sorted() function did not return another string, but a list of characters.

# Evidently, we cannot use the .sort() method on strings, as strings are immutable.
# s.sort()  # AttributeError: 'str' object has no attribute 'sort'
