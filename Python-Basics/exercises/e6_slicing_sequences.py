# In Python, we can obtain a sub-sequence (a slice of a sequence) by
# using the following syntax: [m,n] The slice will contain all elements
# between indexes m (including) and n (excluding).
s = "123456"
l = [1, 2, 3, 4, 5, 6]
t = (1, 2, 3, 4, 5, 6)
# In order to obtain a slice containing the 3rd, 4th, 5th and 6th elements
# of a sequence, we write:
print(s[2:6])  # 3456
print(l[2:6])  # [3, 4, 5, 6]
print(t[2:6])  # (3, 4, 5, 6)
# We can omit m or n and the slice will contain all elements up to one
# extremity.
print(s[:3])    # 123
print(s[3:])    # 456

