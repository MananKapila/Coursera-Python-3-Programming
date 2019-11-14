# As a general rule, you should NOT mutate lists while iterating them.

# If you do, unexpected outcomes might occur.

# Let's take an example where we want to remove all colors beginning with P, B or T from a list.
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois",
          "Peach", "Beige"]
# for position in range(len(colors)):
#     color = colors[position]
#     print(color)
#     if color[0] in ["P", "B", "T"]:
#         del colors[position]
#
# print(colors)
# The code above would give an error: IndexError: list index out of range
# This is because as we delete elements from the list, the size of the list decreases but our position variable will
# still try to go up to the initial list size.
# We can try to fix that by refactoring to:
for color in colors:
    print(color)  # every color in the list will get to be printed here
    if color[0] in ["P", "B", "T"]:
        colors.remove(color)
print(colors)  # ['Red', 'Orange', 'Yellow', 'Green', 'Indigo', 'Violet', 'Pink', 'Teal', 'Peach']
# However, even if we didn't receive an IndexError error this time, we can see that the result does not correspond to
# what we expected. This is because this kind of iteration also uses a behind-the-scenes index for moving to the next
# element and when we remove an element from the list, it moves all the elements one position backwards. Therefore, the
# iteration omits one element for each element removed.
# The conclusion here is that we should NEVER delete or remove elements from a list while iterating over it.

# We now point our attention to a case of appending elements to a list while iterating through it.
# Looking at the following code, we can easily notice that colors starting with a vowel will be appended to the end of
# the list infinitely.
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
# for color in colors:
#     if color[0] in ["A", "E", "I", "O", "U"]:
#         colors.append(color)
# print(colors)

# As a general rule, it is recommended that we do not iterate over a list we will be mutating within the for loop.
