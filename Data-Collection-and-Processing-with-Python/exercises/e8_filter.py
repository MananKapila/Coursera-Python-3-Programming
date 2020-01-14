# Another accumulation pattern that is often used by programmers is building a collection containing some of the
# elements of another collection.
# As in the previous exercise, this can be done by explicit iteration.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)  # [2, 4, 6, 8, 10]


# As was the case with map, Python provides a built-in function that considerably shortens this process. It is called
# filter. It takes as parameters a boolean-returning function and a collection. The boolean returning function is used
# to filter the elements that will end up in the new collection.

def is_even(x):
    return x % 2 == 0


even_numbers = filter(is_even, numbers)
print(even_numbers)  # <filter object at 0x0000020A2E24BB50>
# Just like map, the filter function actually returns an iterable. If we need a list, it is enough to cast it as such.
print(list(even_numbers))  # [2, 4, 6, 8, 10]

# Alternatively, the filter function can receive a lambda expression as first parameter.
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6, 8, 10]
