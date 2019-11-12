# It is also possible to iterate through the indexes of a string or sequence.

# prints:
# t
# h
# i
# s
string = "this"
for i in range(len(string)):
    print(string[i])

# prints:
# 1
# 2
# 3
lst = [1, 2, 3]
for i in range(len(lst)):
    print(lst[i])

# We can use Enumerate, a built-in Python function, to make this proccess easier because
# it allows us to loop through something and have an automatic counter.

# prints:
# 0 apple
# 1 pear
# 2 apricot
# 3 cherry
# 4 peach
lst = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for counter, item in enumerate(lst):
    print(counter, item)
