# When we have nested data structures, especially lists and/or dictionaries, we will frequently need nested for loops
# to traverse them.

# This is a basic example of nested iteration exercise:

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'],
     ['root beer', 'smoothies', 'cranberry juice']]
# Use nested iteration to save every string containing “b” into a new list named b_strings.
b_strings = []
for s in L:
    for ss in s:
        if "b" in ss:
            b_strings.append(ss)
print(b_strings)  # ['bananas', 'blueberries', 'cucumbers', 'green beans', 'root beer', 'cranberry juice']

