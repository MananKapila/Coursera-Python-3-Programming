# Functions can call other functions (it's called composition).

# We can see composition in action in the following example, where we count the letter that appears most  often in a
# string:
# (As a problem-solving strategy, it is helpful to decompose - to design a function by referring to other functions that
# don't yet exist, and then write those functions.)

def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)


def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1
    return d


def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far


print(most_common_letter("abbbbbbbbbbbccccddddd"))  # b


# As a little aside, you may be wondering why it works to have on line 9 a reference to the count_freqs function, which
# has not been defined yet, when we talk about executing Python code from top to bottom. So, we shouldn't be able to
# refer on line 9 to a function that isn't defined until line 13. The reason we don't get an undefined variable error
# is that even though on line 9 we're referring to count_freqs, we don't actually execute line 9, until after we invoke
# on line 31 the most_common_letter function. So, by the time we actually execute line 9, count_freqs has been defined.

# However, if DO call a function before it is defined, we WILL get an error.

# Just by writing this, we get an IDE warning: Unresolved reference to 'function_called_to_early'
# function_called_to_early()
# It causes a runtime error too, namely: NameError: name 'function_to_be_called_too_early' is not defined

def function_called_to_early():
    print("some things")

# What does all that mean for us when we try to understand a program?
# Don’t read from top to bottom. Instead, follow the flow of execution.
# This means that you will read the def statements as you are scanning from top to bottom, but you should skip the body
# of the function until you reach a point where that function is called.
