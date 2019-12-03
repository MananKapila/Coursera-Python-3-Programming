# What happens when two items are “tied” in the sort order? For example, suppose we sort a list of words by their
# lengths. Which five letter word will appear first?
# The answer is that the python interpreter will sort the tied items in the same order they were in before the sorting.

# But what if we wanted to sort them by some other property, say alphabetically, when the words were the same length?
# Python allows us to specify multiple conditions when we perform a sort by returning a TUPLE (instead of a number)
# from the "key" function.

# First, let’s see how python sorts tuples. We’ve already seen that there’s a built-in sort order, if we don’t specify
# any key function. For numbers, it’s lowest to highest. For strings, it’s alphabetic order. For a sequence of tuples,
# the default sort order is based on the default sort order for the first elements of the tuples, with ties being
# broken by the second elements, and then third elements if necessary, etc. For example:
tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]
for tup in sorted(tups):
    print(tup)
# --------------
# ('A', 2, 4)
# ('A', 3, 2)
# ('B', 3, 1)
# ('C', 1, 2)
# ('C', 1, 4)
# --------------

# In the following example, we are going to sort a list of fruit words first by their length, smallest to largest, and
# then alphabetically to break ties among words of the same length. To do that, we have the key function return a tuple
# whose first element is the length of the fruit’s name, and second element is the fruit name itself.
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)
# --------------
# kiwi
# pear
# apple
# mango
# peach
# papaya
# blueberry
# --------------
# We can see that each word was evaluated first on it’s length, then by its alphabetical order. Note that we could
# continue to specify other conditions by including more elements in the tuple.

# But what would happen though if we wanted to sort it by largest to smallest, and then by alphabetical order?
# We might think of using the reverse = True parameter, but that would only solve half the problem, as it won't only
# sort the words from largest to smallest, but also in reverse alphabetical order!
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
for fruit in new_order:
    print(fruit)
# --------------
# blueberry
# papaya
# peach
# mango
# apple
# pear
# kiwi
# --------------
# How can we solve this issue?

# One solution is to add a negative sign in front of len(fruit_name), which will convert all positive numbers to
# negative, and all negative numbers to positive. As a result, the longest elements would be first and the shortest
# elements would be last.
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)
# --------------
# blueberry
# papaya
# apple
# mango
# peach
# kiwi
# pear
# --------------
# We were able to use this trick because we had numerical values. However this wouldn't work for strings.
# If we had two alphabetic properties and we wanted to do reverse on one, and not on the other, it would be harder and
# we wouldn't have any easy solution.

# So summarizing:
# If we want to specify a tie-breaking property, we should have our "key" function return a tuple. Like "key" functions
# everywhere, they always take one item from the sequence as input, but now it's going to return a tuple, where the
# first element of the tuple is the primary property to sort by, the next element is the secondary property to sort by,
# and so on.
