#  We instruct Python to open the olympics.txt file for reading.
# The *open* function creates and returns a file object.
# Here, we assign it to the fileref variable.
fileref = open("olympics.txt", "r")

# additional steps have to be taken to actually read the file

# The *close* function lets Python know that we are done with this file object and it can stop keeping track of it
fileref.close()

# One way to actually read the file is to use the *read* function, which will bring in the entire contents of the file
# as a single string.
fileref = open("olympics.txt", "r")
contents = fileref.read()
fileref.close()
print(contents[:100])  # prints out the first 100 CHARACTERS of the file
# But if we only needed the first 100 characters in the file, it doesn't make sense to read the whole file and keep its
# entire content in memory just for that purpose. Instead, we could only read the first desired characters by passing a
# parameter to the *read* method.
fileref = open("olympics.txt", "r")
contents = fileref.read(100)
print(contents)
fileref.close()
# We will rarely use the *read* method of reading the content of a file all at once, as a big string. Partly because,
# if we had a large file, it would be difficult for our computer to handle all of that in memory all at once.
# We usually use methods that read from the file a little bit at a time and parse its content.

# So instead of getting everything in the file as a single string, we can use the *readlines* method, which returns a
# list of strings - one string for each line in the file.
fileref = open("olympics.txt", "r")
lines = fileref.readlines()
fileref.close()
print(lines[:4])  # prints the first 4 lines of the file, as a list of strings
# ['Name,Sex,Age,Team,Event,Medal\n', 'A Dijiang,M,24,China,Basketball,NA\n', 'A Lamusi,M,23,China,Judo,NA\n',
# 'Gunnar Nielsen Aaby,M,24,Denmark,Football,NA\n']
# We notice that each string in the list ends with a special \n character, which is the newline character.
# If you evaluate a string that contains a newline character you will see the character represented as \n.
# If you print a string that contains a newline you will not see the \n, you will just see its effects (a carriage
# return).
# For a slightly better printout, we can iterate through the array of lines and print each individual line.
for line in lines[:4]:
    print(line)
# Now, we notice in the output that we get blank lines between the actual lines. The reason for this is that the
# *print* function automatically prints its own newline, but it also has to print the newline character at the end of
# each file line.
# If we want to not print the extra newline for each line, we can just apply the *strip* function on each line in our
# print method. We remember that this function removes any whitespace at the beginning and end of a string (by creating
# a new string, of course). Spaces, tabs or newlines are all considered whitespaces.
for line in lines[:4]:
    print(line.strip())
# We can also read a single line from a file by using the *readline* method:
fileref = open("olympics.txt", "r")
line = fileref.readline()
print(line)  # Name,Sex,Age,Team,Event,Medal <with newline>
fileref.close()

# There is, however, a shorter and better way to iterate over all lines of a file.
# It is also the more Pythonic way - instead of reading the whole file into a list and then iterating over that list,
# we can directly iterate through all the lines by treating the file object itself as an iterable.
fileref = open("olympics.txt", "r")
for line in fileref:
    print(line.strip())
fileref.close()
########################################################################################################################
# It is very important to note that iterating over the file object directly is a much more efficient way of parsing a
# file's content than using the *readlines* method, because it reads the content one line at a time, as opposed to
# reading it ALL at once. When dealing with big files, we begin to notice the efficiency gains of this approach.
########################################################################################################################

# Notice that by iterating over the file object directly, we eventually iterate over ALL lines in the file. We can't
# just take a slice of the file, as we did with lists. So this would not have been valid:
# for line in fileref[:4]:
#   print(line.strip())
# Therefore, if we wanted to do something just with the first n lines, we would have to use the *readlines* method.
# But if we're prepared to process all lines, as it is usually the case with files, it's recommended that we use the
# Pythonic way of iterating directly over the file object.

# Another reason why you might want to use *readlines* instead of iterating over the file itself (apart from only
# wanting to take a slice of the file) is that you might want to count how many lines there are in the file.
fileref = open("olympics.txt", "r")
print(len(fileref.readlines()))  # 60
fileref.close()
# An alternative approach could be to iterate over the file object directly and increment a counter each time a new
# line is read.

# If we want to find out how many characters are in the file, we could read the file as a single string and inspect the
# size of this string.
fileref = open("olympics.txt", "r")
print(len(fileref.read()))  # 3178
fileref.close()

# It is very important to note that all these methods of reading a file "use up" the file.
# For example, if we read the first 100 characters:
fileref = open("olympics.txt", "r")
first_100_batch = fileref.read(100)
# and then read another 100 characters
second_100_batch = fileref.read(100)
# , we don't read the same 100 characters twice.
print(first_100_batch == second_100_batch)  # False
# What we actually did was to read characters from 1 to 100, and then from 101 to 200.
# This is because once we open a file, python creates a pointer which keeps track of where we are inside the file and
# with each reading, it moves the pointer accordingly.
fileref.close()
# Similarly, by calling the *readline* method twice on a file, we would read the first two lines of the file (not the
# same one twice).
fileref = open("olympics.txt", "r")
print(fileref.readline())  # Name,Sex,Age,Team,Event,Medal <with newline>
print(fileref.readline())  # A Dijiang,M,24,China,Basketball,NA <with newline>
fileref.close()
# For the same reason, we wouldn't get anything the second time we called *readlines* on a file.
fileref = open("olympics.txt", "r")
print(len(fileref.readlines()))  # 60
print(len(fileref.readlines()))  # 0
fileref.close()

# Now that we have the necessary tools, we can try to parse our olympics.txt file and analyze its data.
# More specifically, we will iterate over the file object and split every line into words, in order to print the details
# of each olympian in a friendly format.
fileref = open("olympics.txt", "r")
for aline in fileref:
    values = aline.split(",")
    print("{} is from {} and is participating in the {} competition".format(values[0], values[3], values[4]))
fileref.close()
