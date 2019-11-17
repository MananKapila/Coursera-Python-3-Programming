# Dictionaries like strings, lists, and tuples are a collection of items. But unlike strings, lists or tuples, they're
# an unordered collection of items meaning that they don't have a first, second or third item.
# They're like a bag of key-value pairs.
# Dictionary keys can only be of immutable types!

# In order to create dictionaries, we use curly braces. This expression creates an empty dictionary:
d = {}
# We set a key-value pair like this:
d['one'] = 'uno'
d['two'] = 'dos'
d['three'] = 'tres'

print(d)  # {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# We can also declare our dictionaries like this:
d = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# This is how we look up a value associated with a particular key.
print(d['one'])  # uno

# The *del* keyword deletes a key-value pair from our dictionary
print(d['two'])  # dos
del d['two']
# print(d['two'])  # KeyError: 'two'

# We can always update the value of a key
print(d['one'])  # uno
d['one'] = 1
print(d['one'])  # 1
# The following is equivalent with d['one'] = d['one'] + 1
d['one'] += 1
print(d['one'])  # 2

########################################################################################################################

d = {"apples": 13, "bananas": 23, "oranges": 4, "kiwis": 59}
# The *len* method gives us the number of key-value pairs in the dictionary.
print(len(d))  # 4

# If we want to obtain the keys of the dictionary, we call the *keys* method, which returns an iterable containing all
# the keys, over which we can loop.
for key in d.keys():
    print("we have {} {}".format(str(d[key]), key))  # example: we have 13 apples
# Because dictionaries are unordered collections, the *keys* method is not guaranteed to return the keys in any
# particular order.

# We notice that the *keys* method does not actually return a list, but a class called dict_keys.
print(d.keys())  # dict_keys(['apples', 'bananas', 'oranges', 'kiwis'])
print(type(d.keys()))  # <class 'dict_keys'>
# If we want to obtain a list of the keys, we need to use the list built-in method:
keys_list = list(d.keys())
print(keys_list)  # ['apples', 'bananas', 'oranges', 'kiwis']
print(type(keys_list))  # <class 'list'>

# However, there is a less verbose way of iterating through the key-value pairs of a dictionary. It is a bit simmilar
# to the way we iterated directly over a file object. In this case, we iterate directly over the dictionary object.
for key in d:
    print("we have {} {}".format(str(d[key]), key))  # example: we have 13 apples

# As there is a method that gives all keys of a dictionary, there is a method that returns all values in the dictionary:
print(d.items())  # dict_items([('apples', 13), ('bananas', 23), ('oranges', 4), ('kiwis', 59)])
print(type(d.items()))  # <class 'dict_items'>
print(list(d.items()))  # [('apples', 13), ('bananas', 23), ('oranges', 4), ('kiwis', 59)]
print(type(d.items()))  # <class 'list'>
# We notice that by converting the *item* method's result to a list, we obtain a list of key and value tuples.

# We can also check whether a key is inside a dictionary by using the *in* keyword:
print('apples' in d)  # True
print('strawberries' in d)  # False
if 'kiwis' in d:
    print("we have kiwis")
else:
    print("we have no kiwis")

# We've seen that we can get the value of a key from a dictionary by indexing:
print(d['apples'])  # 13
# d['cherries']
# If 'cherries' is not a key in the dictionary, the execution of our script will be terminated by an error:
# KeyError: 'cherries'
# However, there is a second, better way of accessing the value of a key - using the *get* method.
print(d.get('apples'))  # 13
print(d.get('cherries'))  # None
# We notice that, even though 'cherries' is not a key in this dictionary, we did not get an error. The *get* method
# simply returned None, without interrupting the program.
# Moreover, we can specify a second optional parameter to *get*, which instructs it to return a certain fallback value,
# in case the key is absent.
print(d.get('cherries', 0))  # 0
print(d.get('apples', 0))  # 13

# We now take a look at dictionary aliases and how they both point to the same space in memory.
d1 = {1: 'white', 2: 'blue', 3: 'yellow'}
# ======= Memory =======
# d1    ----- {1: 'white', 2: 'blue', 3: 'yellow'}
# ======================
d2 = d1  # we created an alias for d1
# ======= Memory =======
# d1    ----- {1: 'white', 2: 'blue', 3: 'yellow'}
# d2    ____/
# ======================
print(d1 is d2)  # True
d1[1] = 'black'
# ======= Memory =======
# d1    ----- {1: 'black', 2: 'blue', 3: 'yellow'}
# d2    ____/
# ======================
print(d2[1])  # black
