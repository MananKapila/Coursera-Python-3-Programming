# We've seen that the map and filter functions offer solutions for needs that arise very often in the world of
# programming. However, python provides another special, even simpler syntax that circumvents the use of these
# functions, while obtaining the same results.

# This alternative way to do map and filter operations is called a list comprehension. It's a concise way to create
# lists from other lists. The general syntax is:
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
# It's important to note that the if-clause is optional!

# Let's see this syntax in action:
numbers = [2, 5, 9]
lst = [value * 2 for value in numbers]
print(lst)  # [4, 10, 18]

# Let's introduce an if-clause too in the equation.
lst = [value * 2 for value in numbers if value % 2 == 1]
print(lst)  # [10, 18]


# Of course, we can also use functions inside list comprehensions:

def double(x):
    return x * 2


def odd(x):
    return x % 2 == 1


lst = [double(value) for value in numbers if odd(value)]
print(lst)  # [10, 18]

# Let's do some exercises using list comprehensions :)

# 1. The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to
# accomplish the same thing. Assign it to the variable lst2. Only one line of code is needed.

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)  # [12, 34, 21, 42]
lst2 = [n for n in L if n > 10]
print(lst == lst2)  # True

# 2. Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the
# dictionary tester. Do this using a list comprehension.

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
# In order to better see the structure of the tester variable, we can use the dumps from the json library.
import json

print(json.dumps(tester, indent=2))
# Now we can better see that the solution to this exercise is:
compri = [v['name'] for v in tester['info']]
print(compri)  # ['Lauren', 'Ayo', 'Kathryn', 'Nick', 'Gladys', 'Adam']

# 3. Define a function that takes a list of strings as parameter and returns a list containing the lengths of those
# strings that are longer than 4 characters. Solve this exercise in three ways.

strings = ["a", "bc", "def", "ghij", "klmno", "pqrs", "tuvwxyz"]


# First, we could use the old "honest" approach of iterating and accumulating.
def f1(lst):
    to_return = []
    for s in lst:
        if len(s) >= 4:
            to_return.append(len(s))
    return to_return


print(f1(strings))  # [4, 5, 4, 7]


# The second way could be using the map and filter functions.

def f2(lst):
    to_map = filter(lambda x: len(x) >= 4, lst)
    return list(map(len, to_map))


print(f2(strings))  # [4, 5, 4, 7]


# And finally, the third way is by using list comprehensions.

def f3(lst):
    return [len(s) for s in lst if len(s) >= 4]


print(f3(strings))  # [4, 5, 4, 7]
