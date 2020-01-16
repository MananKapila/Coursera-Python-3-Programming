# One more common pattern with lists, besides accumulation, is to step through a pair of lists (or several lists),
# doing something with all of the first items, then something with all of the second items, and so on.
# The following section of code is an example of this:

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)  # [4, 6, 8]

# However, this way of doing things is somewhat obscuring the purpose of our code. Python provides a simpler, elegant
# function for this purpose, called zip.

# The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like
# lists for most practical purposes), pairing up all the first items as one tuple, all the second items as a tuple, and
# so on. Then we can iterate through those tuples, and perform some operation on all the first items, all the second
# items, and so on.

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L4 = list(zip(L1, L2))
print(L4)  # [(3, 1), (4, 2), (5, 3)]

# Here's what happens when we loop through the tuples:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))

for (x1, x2) in L4:  # notice that we are using the tuple unpacking mechanism built into python here
    L3.append(x1 + x2)

print(L3)  # [4, 6, 8]

# Or, simplifying and using a list comprehension:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)  # [4, 6, 8]

# Let's do a couple of exercises highlighting the usefulness of the zip function.

# 1. Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3,
# that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can be
# accomplished in one line of code.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for (x1, x2) in zip(L1, L2) if x1 > 10 and x2 < 5]


# 2. Consider a function called possible, which determines whether a word is still possible to play in a game of
# hangman, given the guesses that have been made and the current state of the blanked word.
# Below we provide function that fulfills that purpose. In order to make it a bit more comprehensible, rewrite it using
# the zip function.

def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True


print(possible("wonderwall", "_on__r__ll", "otnqurl"))  # True
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))  # False


def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True


print(possible("wonderwall", "_on__r__ll", "otnqurl"))  # True
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))  # False
