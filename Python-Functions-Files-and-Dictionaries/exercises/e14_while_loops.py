# There is another Python statement that can also be used to build an iteration. It is called the while statement.
# The while statement provides a much more general mechanism for iterating. Similar to the if statement, it uses a
# boolean expression to control the flow of execution. The body of while will be repeated as long as the controlling
# boolean expression evaluates to True.
# We can use the while loop to create any type of iteration we wish, including anything that we have previously done
# with a for loop. Actually, any for loop can be rewritten as a while loop.

# For example, let's take this function, which uses a for-loop:
def for_sum_to(aBound):
    """ Return the sum of 1+2+3 ... n """
    sum = 0
    for i in range(aBound + 1):
        sum += i
    return sum


def while_sum_to(aBound):
    """ Return the sum of 1+2+3 ... n """
    sum = 0
    i = 1
    while i <= aBound:
        sum += i
        i += 1
    return sum


print(for_sum_to(100))  # 5050
print(while_sum_to(100))  # 5050

# We advise using a for loop whenever it will be known at the beginning of the iteration process how many times the
# block of code needs to be executed.
# When is it not known at the beginning of the iteration how many times the code block needs to be executed? The answer
# is, when it depends on something that happens during the execution.
# One very common pattern is called a LISTENER loop. Inside the while loop there is a function call to get user input.
# The loop repeats indefinitely, until a particular input is received.

theSum = 0
x = -1
while x != 0:
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x
print(theSum)


# The following function is also an example of a listener loop. We keep asking the user for item prices and we keep
# adding them to a total price. The loop exits when the user inputs a zero price, and that's when we compute and return
# the average item price.
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)


checkout()


# You can also use a while loop when you want to validate input!
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()  # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer


response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')


# We can break out of the while loop by using the *break* keyword:
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.")
# this phrase will always print
# We are done with the while loop.

# We can tell the while loop to ignore the rest of the current iteration and jump to the next iteration by using the
# *continue* keyword:
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: " + str(x))
# we are incrementing x
# we are incrementing x
# we are incrementing x
# Done with our loop! X has the value: 15
