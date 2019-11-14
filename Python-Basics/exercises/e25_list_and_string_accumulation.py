# We've seen the accumulator pattern with numbers.
# Now we're going to see a couple of ways in which it can be applied to lists and strings.

# We accumulate the squares of a list's elements into another list
lst = [3, 5, 8]
acc = []
for w in lst:
    x = w ** 2
    acc.append(x)
print(acc)  # [9, 25, 64]

# We input a string and want to duplicate its letters and insert dashes between them.
s = input("Enter some text: ")
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"
print(ac) # for s = "math", it prints m-m-a-a-t-t-h-h-
