a = 3
b = a + 5
if a < b:
    print("a is less than b")  # goes in here
else:
    print("a is not less than b")

# *if* statements can be unary (they don't need to be accompanied by the else statement).
# The following block will not print anything.
# Side-note: the parentheses are not necessary, but it is still valid syntax.
a = b - 1
if (a > b):
    print("a is bigger than b")

# When we have an if statement inside another if statement, we call that nested conditionals.
b = a + 11
if a < b:
    if b - a > 10:
        print("the difference is quite big")  # goes in here

a = 10
b = 3
if a < b:
    print("a is less than b")
else:
    if a > b:
        print("a is greater than b")  # goes here
    else:
        print("a and b must be equal")

# When a nested *if* statement is the only code inside an *else* clause (as above), we
# can simplify our code by using the *elif* statement (which chains an *else* and an *if* ).
# We call these constructs chained conditionals:

a = b
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a and b must be equal")  # goes here

# We now see an example of the accumulator pattern which uses a conditionals.
# We want to count the number of vowels in a string.
string = "what's up with this string"
vowels_no = 0
for s in string:
    if s in ['a', 'e', 'i', 'o', 'u']:
        vowels_no += 1
print(vowels_no)  # 5
