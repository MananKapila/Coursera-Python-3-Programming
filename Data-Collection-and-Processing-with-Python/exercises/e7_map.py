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

# One disadvantage of iterators is that after we iterate over all their elements, we cannot get anything from them
# anymore (we can't loop over them again). Because of this, whenever we need to iterate over an iterator multiple
# times, we should turn it into a list.
# (By the way, the conversion of an iterator into a list already "exhausts" the iterator by accessing all of its
# elements behind the scenes. This renders the iterator useless, as it can't provide anything anymore. That's why the
# second time we convert an iterator into a list, the result is an empty list).

vars = [1, 2, 3, 4]
a_map = map(lambda x: x * 2, vars)
list_from_map = list(a_map)
print(list_from_map)  # [2, 4, 6, 8]
second_list_from_map = list(a_map)
print(second_list_from_map)  # []

import collections.abc

# Side note: mind the difference between an iterator and an iterable!
print(isinstance(a_map, collections.abc.Iterator))  # True
# print(map_result[0]) - we would get a TypeError: 'map' object is not subscriptable
print(isinstance(list_from_map, collections.abc.Iterator))  # False

print(isinstance(a_map, collections.abc.Iterable))  # True
print(isinstance(list_from_map, collections.abc.Iterable))  # True

# Quote: "Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method.
# Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators have
# __next__() method, which returns the next item of the object."
# (https://www.geeksforgeeks.org/python-difference-iterable-iterator/)
