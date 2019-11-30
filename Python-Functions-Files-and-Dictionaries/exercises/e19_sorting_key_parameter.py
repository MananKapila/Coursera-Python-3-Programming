# We saw earlier how the sorted() function can receive an optional parameter called "reverse", in order to sort the
# collection in reverse order.

# We will now see the other optional parameter that sorted() can take - the "key" parameter. Through it, we specify we
# want to sort things in some order other than the 'natural' one or or its reverse.
# Therefore, the "key" parameter is supposed to be a function. This function should return a number for any given
# element in the collection. These numbers will be used by the sorted() function to sort the elements.

# Let's see a couple of examples.

# Example 1 ============================================================================================================
# Suppose we want to sort a list of numbers based on their absolute value.
l = [-3, 16, 2, 33, -54]
print(sorted(l))  # [-54, -3, 2, 16, 33] - this is now what we want


# We therefore have to define a function which computes the absolute value of any number.
def abs(x):
    if x < 0:
        return -x
    else:
        return x


print(sorted(l, key=abs))  # [2, -3, 16, 33, -54] - this is what we want
# We notice that we could sort the list based on the absolute values in reverse, by using both optional parameters of
# the sorted() function.
print(sorted(l, key=abs, reverse=True))  # [-54, 33, 16, -3, 2]

# Example 2 ============================================================================================================
# Suppose we have a dictionary with strings as the keys and numbers as the values.
d = {"hey": 3, "there": 5, "guys": 4}
print(sorted(d))  # ['guys', 'hey', 'there']


# Instead of sorting the dictionary keys in alphabetic order, we might like to sort them based on their values.
# We therefore have to define a function which returns the value of a key in our dictionary:
def key_value(k):
    return d[k]


print(sorted(d, key=key_value))  # ['hey', 'guys', 'there']

# Example 3 ============================================================================================================
# Below, we have provided a list of strings called nums.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']


# We should be able to write a function called last_char that takes a string as input and returns only its last
# character. We should use this function to sort the list nums by the last digit of each number, from lowest to highest,
# and save this as a new list called nums_sorted.
def last_char(s):
    return int(s[len(s) - 1])


nums_sorted = sorted(nums, key=last_char)
print(nums_sorted)  # ['1450', '871', '32', '33', '44', '1005', '16', '8907', '14378', '19']

# Example 4 ============================================================================================================
# As we learned in e16, we can use anonymous functions using lambda expressions.
# Let's solve the previous exercise by using an anonymous function instead.

# This is the way to do it:
nums_sorted = sorted(nums, key=lambda s: int(s[len(s) - 1]))
print(nums_sorted)  # ['1450', '871', '32', '33', '44', '1005', '16', '8907', '14378', '19']

# We could also do it in this silly way:
nums_sorted = sorted(nums, key=lambda s: last_char(s))
print(nums_sorted)  # ['1450', '871', '32', '33', '44', '1005', '16', '8907', '14378', '19']
