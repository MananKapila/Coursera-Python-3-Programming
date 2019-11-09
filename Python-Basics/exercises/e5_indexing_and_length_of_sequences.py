# Strings, lists and tuples are sequences.
# Their elements can be accessed through indexes, in the same way.
# Indexes start (from left to right) with 0.
str = "a string"
print(str[0])   # a
print(str[3])   # t
lst = [1, 2, 3, 4]
print(lst[2])   # 3
tpl = (1, 2, 3)
print(tpl[2])   # 3

# In Python, we can specify negative indexes, such as [-i].
# They represent the i element from right to left.
# Note that negative indexes start with -1, as negative 0 doesn't exist.
print(str[-1])  # g
# print(str[-10]) # error
print(lst[-2])  # 3
print(tpl[-3])  # 1

# We can obtain the lengths of any sequence with the len built-in function
print(len(str)) # 8
print(len(lst)) # 4
print(len(tpl)) # 3

# We notice that str[len(str) - 1] is equivalent with str[-1]
boolean = str[len(str) - 1] == str[-1]
print(boolean)  # true
