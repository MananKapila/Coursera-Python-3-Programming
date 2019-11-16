# Python has the notion of a context manager that automates the process of doing common operations at the start of some
# task, as well as automating certain operations at the end of some task. For reading and writing a file, the normal
# operation is to open the file and assign it to a variable. At the end of working with a file the common operation is
# to make sure that file is closed.
# We can see the context manager in action by considering the *with* statement.
# The general form of a *with* statement is:

# with <create some object that understands context> as <some name>:
#     do some stuff with the object

# When the program exits the with block, the context manager handles the common stuff that normally happens at the end.

# In the case of opening a file, the *with* statement can be used in this way:
with open('olympics.txt', 'r') as f:
    for line in f:
        print(line)
# The first line of the with statement opens the file and assigns it to the variable f.
# Then we can iterate over the file in any of the usual ways.
# When we are done we simply stop indenting and let Python take care of closing the file and cleaning up.

# The block of code above is equivalent to:
f = open('olympics.txt', 'r')
for line in f:
    print(line)
f.close()