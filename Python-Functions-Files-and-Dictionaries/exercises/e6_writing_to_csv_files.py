# Let's say we have a list of tuples, where each tuple could represent a CSV row.
# We want to write this information into a file, while respecting the CSV standard.

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("olympics_out.csv", "w")
# We would first need to write the header row and a newline.
outfile.write('Name,Age,Sport')
outfile.write('\n')
# Then, we would have to print the rows.
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    # Tip: Later, we will see that python provides an advanced technique for automatically unpacking the
    # three values from the tuple, with .format(*olympian).
    row_string = '{},{},{}'.format(*olympian)
    # Theoretically, another way of creating row_string would be to use the *join* method. We remember that *join* is
    # the opposite of the *split* method, and it expects a sequence of strings as argument.
    # But this would not work for our current example:
    # row_string = ",".join(olympians[0])
    # ...because our tuples also contain integers, so we would get an exception.
    # Another way to create row_string would be string concatenation, but this is the least preferred approach, as it
    # is cumbersome and hard to read.
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

# As described previously, if one or more columns contain text, and that text could contain commas, we need to do
# something to distinguish a comma in the text from a comma that is separating different values (cells in the table).
# If we want to enclose each value in double quotes, it can start to get a little tricky, because we will need to have
# the double quote character inside the string output. But it is doable. Indeed, one reason Python allows strings to be
# delimited with either single quotes or double quotes is so that one can be used to delimit the string and the other
# can be a character in the string. If you get to the point where you need to quote all of the values, we recommend
# learning to use python’s csv module.

olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("olympics2_out.csv","w")
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
