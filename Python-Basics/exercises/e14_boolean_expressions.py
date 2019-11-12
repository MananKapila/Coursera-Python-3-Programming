# In Python, boolean values are written with a capital first letter: True and False

a = 5
print(a == 6)  # False
print((a == 5) is True)  # True
print((a == 5) == True)  # True (the syntax above is preferred)
print(type(True))  # <class 'bool'>

# Boolean logical operators are: or, and, not

print(not (a == 6))  # True
print(a > 0 and a < 3)  # False
# The comparison above can be simplified to a chain comparison syntax:
print(0 < a < 3)  # False
