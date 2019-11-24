# Mutating an object means changing its state.
# In Python, some objects are mutable, which means we can perform changes directly on them.
# Other objects are immutable, which means that any attempt to change them will
# instead result in a modified copy of the original object.

# Lists are mutable
lst = ["apple", "banana", "cherry"]
# In memory, we have this:
# ======= Memory =======
# lst ----- ["apple", "banana", "cherry"]
# ======================
lst[0] = "pear"
lst[-1] = "watermelon"
# We still have one list in memory, and the "apple" and "banana" elements have been
# completely replaced by "pear" and "watermelon"!
# ======= Memory =======
# lst ----- ['pear', 'banana', 'watermelon']
# ======================
lst = [0, 1, 2, 3, 4, 5, 6, 7]
lst[3:5] = [100, 100]
# ======= Memory =======
# lst ----- [0, 1, 2, 100, 100, 5, 6, 7]
# ======================
# Side-note: we don't have to replace a slice of a sequence with a list of the same size as the slice.
# This means we can use slices of sequences to delete or add elements to them.
lst[3:5] = []
# ======= Memory =======
# lst ----- [0, 1, 2, 5, 6, 7]
# ======================
lst[3:5] = [1, 1, 1, 1, 1]
# ======= Memory =======
# lst ----- [0, 1, 2, 1, 1, 1, 1, 1, 7]
# ======================

# Strings are  immutable!
# If we try to change a portion of a string, we get an error.
string = "you cannot change me!"
# string[0] = "l"
# TypeError: 'str' object does not support item assignment
# string[4:8] = "ok"
# TypeError: 'str' object does not support item assignment
# If we want to obtain a string based on another one, we have to create a new string!
new_string = "they" + string[3:]
print(new_string)  # they cannot change me!
# ======= Memory =======
# string        ----- "you cannot change me!"
# new_string    ----- "they cannot change me!"
# ======================
first_str = "hello"
second_str = first_str
# first_str and second_str initially point to the same the same location in memory.
print(id(first_str) == id(second_str))  # True
# ======= Memory =======
# first_str     ----- "hello"
# second_str    ____/
# ======================
second_str = "goodbye"
# But after this assignment, only second_str will point to "goodbye". The two references will point to different strings
# in memory.
print(first_str)  # hello
print(second_str)  # goodbye
# ======= Memory =======
# first_str     ----- "hello"
# second_str    ----- "goodbye"
# ======================
print(id(first_str) == id(second_str))  # False

# The same goes with numbers.
a = -3
b = a
b = 10
print(a)  # -3
print(b)  # 10

# Tuples are immutable.
# As with strings, if we try to use item assignment to modify one of the elements of a tuple, we get an error.
# In fact, that’s the key difference between lists and tuples: tuples are like immutable lists.
# None of the operations on lists that mutate them are available for tuples.
# Once a tuple is created, it can’t be changed.
tpl = (1, 2, 3)
# tpl[0] = 5
# TypeError: 'tuple' object does not support item assignment
