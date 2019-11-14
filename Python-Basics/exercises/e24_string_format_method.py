# Often times, we need to make cumbersome string concatenations (for example, for personalizing messages)
from builtins import print

namesAndScores = [("Keith", 100), ("Marcus", 80), ("Emma", 50)]
for tpl in namesAndScores:
    print("Hello, " + tpl[0] + ", your score is " + str(tpl[1]))
# The above loop prints:
# Hello, Keith, your score is 100
# Hello, Marcus, your score is 80
# Hello, Emma, your score is 50

# Instead, we can use the format method, which lets group the plug-in strings in one place, outside the base string.
for tpl in namesAndScores:
    print("Hello, {}, your score is {}".format(tpl[0], tpl[1]))
# This prints the same thing as before but this time, the generic message is in one piece and is easier to read.

# The format method also takes numbers as parameters (we've seen above that we didn't need to convert tpl[1] to string).
# In the case of floating point numbers, the algorithm behind the format method decides how many decimal places to show.
origPrice = float(input('Enter the original price: '))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount / 100) * origPrice
calculation = '{} discounted by {} percent is {}.'.format(origPrice, discount, newPrice)
print(calculation)  # 123.0 discounted by 19.0 percent is 99.63000000000001.

# However, we can specify the precision with which we want to display floating point numbers.
origPrice = float(input('Enter the original price: '))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount / 100) * origPrice
calculation = '{:.2f} discounted by {} percentage is {:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)  # 123.00 discounted by 19.0 percentage is 99.63.

# It's important to give the same number of arguments as the base string is waiting for.
name = "Hannah"
age = 32
# print("Hi, my name is {} and my age is {}".format(name)) # This gives an error

# If we don't format a string, we can use braces as much as we want in a string, without fearing that they will have any
# special meaning.
print("These {} { brackets } are not confusing at all {} }} {{ { } ")
# prints the string exactly as given

# However, if we want to use the format function on a string, then we have to escape "innocent" brackets.
# We do that by doubling them. Instead of { we use {{ and instead of } we use }}.
a = 3
b = 4
# print("This set has the following values { {}, {} }".format(a,b)) # prints an error
print("This set has the following values {{ {}, {} }}".format(a, b))
# prints: This set has the following values { 3, 4 }
