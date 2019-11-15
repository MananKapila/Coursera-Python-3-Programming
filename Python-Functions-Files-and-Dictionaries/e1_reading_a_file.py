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
# We will rarely use this method of reading the content of a file all at once, as a big string. Partly because, if we
# had a large file, it would be difficult for our computer to handle all of that in memory all at once.
# We usually use methods that read from the file a little bit at a time and parse its content.

# So instead of getting everything in the file as a single string, we can use the *readlines* method, which returns a
# list of strings - one string for each line in the file.
fileref = open("olympics.txt", "r")
lines = fileref.readlines()
fileref.close()
print(lines[:4])    # prints the first 4 lines of the file, as a list of strings
# ['Name,Sex,Age,Team,Event,Medal\n', 'A Dijiang,M,24,China,Basketball,NA\n', 'A Lamusi,M,23,China,Judo,NA\n',
# 'Gunnar Nielsen Aaby,M,24,Denmark,Football,NA\n']
# We notice that each string in the list ends with a special \n character, which is the newline character.
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

