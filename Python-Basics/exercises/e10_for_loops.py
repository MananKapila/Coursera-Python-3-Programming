# Iteration over sequences can be done with for loops
lst = [1, 2, 3, 4]
# prints:
# 2 piglets
# 3 piglets
# 4 piglets
# 5 piglets
for var in lst:
    var += 1
    print(var, "piglets")

tpl = (1, 2, 3)
# the accumulator pattern
sum = 0
for nr in tpl:
    sum += nr
print(sum)      # 6

# When a for loop is used over a string, each of the string's characters is
# assigned to the loop variable.

# prints:
# h
# e
#
# l
# l
# o
string = "he llo"
for char in string:
    print(char)

