# JSON stands for JavaScript Object Notation. It looks a lot like the representation of nested dictionaries and lists
# in python when we write them out as literals in a program, but with a few small differences (e.g., the word null
# instead of None). When your program receives a JSON-formatted string, generally you will want to convert it into a
# python object, a list or a dictionary.

# Again, python provides a module for doing this. The module is called json. We will be using two functions in this
# module, loads() and dumps().
# It's worth noting that their names stand for "load string" and "dump string". It's useful to keep that in mind as a
# quick mnemonic regarding what they do.

import json

# ======================================================================================================================
# json.loads() takes a string as input and produces a python object/dictionary/list/etc as output.

# Consider, for example, some data that we might get from Apple’s iTunes, in the JSON format:
a_string = '{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
d = json.loads(a_string)
print(type(d))  # <class 'dict'>
print(d)  # {'resultCount': 25, 'results': [{'wrapperType': 'track', 'kind': 'podcast', 'collectionId': 10892}]}
print(d.keys())  # dict_keys(['resultCount', 'results'])
print(d['resultCount'])  # 25
# print(a_string['resultCount']) This would obviously result in an error, because a_string is not a dictionary.

# ======================================================================================================================
# The other function we will use is dumps(). It does the inverse of loads(). It takes a python object/dictionary/list
# and returns a string, in JSON format.
d = {'key1': {'c': True, 'a': 90, 5: 50}, 'key2': {'b': 3, 'c': "yes"}}
json_string = json.dumps(d)
print(json_string)  # {"key1": {"c": true, "a": 90, "5": 50}, "key2": {"b": 3, "c": "yes"}}

# dumps() has a few other parameters. Two useful ones are "sort_keys" and "indent".

# When the value True is passed for the "sort_keys" parameter, the keys of dictionaries are output in alphabetic order
# (along with their values, of course).
# sorted_json_string = json.dumps(d, sort_keys=True) TypeError: '<' not supported between instances of 'int' and 'str'
# Trying to sort the json content by keys using the current d dictionary would result in the above error because we
# have keys of mixed types.
d = {'key1': {'c': True, 'a': 90, "5": 50}, 'key2': {'b': 3, 'c': "yes"}}
sorted_json_string = json.dumps(d, sort_keys=True)
print(sorted_json_string)  # {"key1": {"5": 50, "a": 90, "c": true}, "key2": {"b": 3, "c": "yes"}}

# The "indent" parameter expects an integer representing the number of spaces to be used for indentation. When "indent"
# is provided, dumps generates a string suitable for displaying to people, with newlines and indentation.
sorted_pretty_json_string = json.dumps(d, sort_keys=True, indent=2)
print(sorted_pretty_json_string)
# {
#   "key1": {
#     "5": 50,
#     "a": 90,
#     "c": true
#   },
#   "key2": {
#     "b": 3,
#     "c": "yes"
#   }
# }
