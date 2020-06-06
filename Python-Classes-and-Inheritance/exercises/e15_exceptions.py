# An exception is a signal that a condition has occurred that can’t be easily handled using the normal flow-of-control
# of a Python program. They provide us with way way to have a non-sequential point where we can handle something out of
# the ordinary (exceptional).
# Exceptions are often defined as being “errors” but this is not always the case.
# All errors in Python are dealt with using exceptions, but not all exceptions are errors!

# The try/except control structure provides a way to process a run-time error and continue on with program execution.
# This way, when Python encounters a run-time error, instead of stopping the whole program and printing the error, it
# just jumps to the 'except' block and executes whatever is inside it (without printing the error in the console).

lst = [0, 1, 2]
print(lst[3])  # This results in a runtime error that stops the whole program: "IndexError: list index out of range"

try:
    print("Trying to access element with index 3")  # This line gets printed
    print(lst[3])  # Instead of stopping the program, Python just moves to the 'except' block instead
    print("There it was.")  # This line and the one above don't get printed.
except:
    print("There is no element with index 3")  # This line gets printed

try:
    print("Trying to access element with index 2")  # This line gets printed
    print(lst[2])  # This line prints "2"
    print("There it was.")  # This line gets printed
except:
    print("There is no element with index 2")  # This line doesn't get printed

# After the word 'except', there can optionally be a specification of the kinds of errors that will be handled.
# The catchall is the class Exception. If you write 'except Exception:', all runtime errors will be handled.
# If you specify a more restricted class of errors, only those errors will be handled; any other kind of error will
# still cause the program to stop running and an error message to be printed.

# For example, the following 'except' block will not catch the ZeroDivisionError:
try:
    a = 5 / 0  # Python stops the program and prints 'ZeroDivisionError: division by zero'.
except IndexError:
    print("We caught an index error")  # This line doesn't get printed

# The exception code can access a variable that contains information about exactly what the error was.
# Thus, for example, in the 'except' clause, you could print out the information that would normally be printed as an
# error message but continue on with execution of the rest of the program. To do that, you specify a variable name
# after the exception class that’s being handled. The exception clause code can refer to that variable name.

try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")  # This line doesn't get printed
except Exception as e:
    print("We got an error and we will print it without interrupting the program")  # This line gets printed
    print(e)  # This line prints "list index out of range"
    print(e.__class__)  # This line prints "<class 'IndexError'>"

print("continuing")  # This line gets printed
