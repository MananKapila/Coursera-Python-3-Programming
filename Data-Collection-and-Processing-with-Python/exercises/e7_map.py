# Sometimes, we want to apply the same function to all the elements of a collection.
# We could do that by looping through the collection.

numbers = [1, 2, 3]


def double(n):
    return 2 * n


doubles = []
for n in numbers:
    doubles.append(double(n))
print(doubles)  # [2,4,6]

# Actually, the need of repeatedly applying certain functions to all the elements of a collection is so common that
# Python has a built in function just for that: map. It takes two arguments: the function to apply and the collection.
# (Its purpose is the same as the map method in Java 8)

doubles = map(double, numbers)
print(doubles)  # <map object at 0x7f49a2056a20>
print(type(doubles))  # <class 'map'>
# The reason we get this result is that technically, the map function produces an “iterator”, which is like a list but
# produces the items as they are needed. Most places in Python where we can use a list (e.g., in a for loop), we can
# also use an “iterator” as if it was actually a list.
# If we ever need a list, we can transform the "iterator" to a list by casting it as such.
print(list(doubles))  # [2,4,6]

# Instead of passing a previously defined function as first parameter, we can construct an ad-hoc lambda function.
print(numbers)  # [1, 2, 3] - we notice that the original list remained the same
doubles = map(lambda x: 2 * x, numbers)
print(list(doubles))  # [2, 4, 6]
