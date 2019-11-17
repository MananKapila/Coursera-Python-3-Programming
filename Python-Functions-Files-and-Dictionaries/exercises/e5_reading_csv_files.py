# CSV is a file format which stands for Comma Separated Values.
# A valid CSV file has the same number of commas on every line.
# Most operating systems will, by default, try to open CSV files as excel spreadsheets.

# We've already parsed a CSV file at the end of e1, becuase our olympics.txt file adheres by the CSV format.
fileref = open("olympics.txt", "r")
for aline in fileref:
    values = aline.split(",")
    print("{} is from {} and is participating in the {} competition".format(values[0], values[3], values[4]))
fileref.close()

# Notice that we split the rows into columns using comma as a delimiter. One issue we might run into is that some of the
# columns might themselves contain commas. How will a program processing a .csv file know when a comma is separating
# columns, and when it is just part of the text string giving a value within a column?
# The CSV format is actually a little more general than we have described and has a couple of solutions for that
# problem. One alternative format uses a different column separator, such as | or a tab (t). Sometimes, when a tab is
# used, the format is called tsv, for tab-separated values). If we get a file using a different separator, we can just
# call the .split('|') or .split('\\t').
# The other advanced CSV format uses commas to separate but encloses all values in double quotes. For example, one row
# of data might look like this:
# "Edgar Lindenau Aabye","M","34","Denmark/Sweden","Tug-Of-War","Gold"
# If we are reading a .csv file that has enclosed all values in double quotes, it’s actually a pretty tricky programming
# problem to split the text for one row into a list of values. We won’t want to try to do it directly. Instead, we
# should use python’s built-in csv module.
