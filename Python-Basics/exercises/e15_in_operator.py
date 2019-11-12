# Another logical operator is *in*. It checks whether an element is contained in a sequence.
# It thus works with strings, lists, tuples, etc.

s = "apple"
print("a" in s)  # True
print("ppl" in s)  # True
print("sql" in s)  # False

# Strangely enough, the empty string is considered to be contained in any string
print("" in s)  # True
print("" in "")  # True

lst = [1, "hi", [3, 4]]
print(1 in lst)  # True
print([3, 4] in lst)  # True

# The opposite expression of *in* is *not in*
print(1 not in lst)  # False
print(2 not in lst)  # True
print("ea" not in "great")  # False
print("fg" not in "great")  # True

# It's important to note that the *not* in the *not in* and the usual *not*
# logical operator are completely unrelated things.
