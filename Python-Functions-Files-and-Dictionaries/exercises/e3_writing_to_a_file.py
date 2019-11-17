# In order to write to a file, you need to open the file and pass 'a' or 'w' as second parameter.

fw = open("../my_data/squares.txt", "a")
# Here, 'a' stands for append. By opening a file this way, the text we're going to write will be APPENDED in
# continuation to any previous content the file might have had before.

fw = open("../my_data/squares.txt", "w")
# Here, 'w' stands for writing. By opening a file this way, the text we're going to write will REPLACE any content the
# file might have previously had.

# When opening a file for writing/appending, if the file doesn't already exist, the *open* function will create it.

# We use the *write* function for writing to a file.
fw.write("We begin listing the squares of integers less than 13: \n")
for i in range(13):
    fw.write(str(i ** 2) + " ")
fw.close()

# We can now read from this file
fr = open("../my_data/squares.txt", "r")
print(fr.readlines()[1][:7])    # reads the first 7 characters of the second line
# prints: 0 1 4 9
fr.close()

