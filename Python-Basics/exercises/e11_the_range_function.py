# The range function is useful for quickly enforcing a specific number of iterations.
# In its basic for, the range function takes to parameters: range(start, end)
# It returns an *iterable* made out of sorted integers, starting with <start>
# and ending with <end> - 1.
# We notice that, as in the case of slices, the start is inclusive and the end
# is exclusive.

for i in range(3, 8):
    print(i)
# has the same effect as:
for i in [3, 4, 5, 6, 7]:
    print(i)

# The range function can take only one parameter as well: range(end). This means
# that the start is implicitly 0.

for i in range(3):
    print(i)
# has the same effect as:
for i in [0, 1, 2]:
    print(i)

# The range function can also take three parameters: range(start, end, step).
# The third parameter represents the size of the incremental steps with
# which we obtain numbers between the [start, end) interval.

# prints:
# 10
# 25
# 40
for i in range(10, 50, 15):
    print(i)

# The range function can only take integers as parameters.

# Even though iterating through a range can be thought of as iterating over a list,
# the range function does *not* return a list! It returns an iterable.
# In order to obtain an actual list from the range function, we need to cast its result.

print(type(range(1, 3)))  # <class 'range'>
print(type(list(range(1, 3))))  # <class 'list'>
