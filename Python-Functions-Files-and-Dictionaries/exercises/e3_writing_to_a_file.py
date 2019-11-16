# In order to write to a file, you need to open the file and pass 'w' as the second parameter.
fw = open("../my_data/squares.txt", "w")
# When opening a file for writing, if the file doesn't already exist, the *open* function will create it.

# The *write* function adds content at the end of the file.
fw.write("We begin listing the squares of integers less than 13: \n")
for i in range(13):
    fw.write(str(i ** 2) + " ")
fw.close()

# We can now read from this file
fr = open("../my_data/squares.txt", "r")
print(fr.readlines()[1][:7])    # reads the first 7 characters of the second line
# prints: 0 1 4 9
fr.close()
