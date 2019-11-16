# If the file you need to open resides in the same directory as your Python script, you can simply pass the filename to
# the *open* function. Otherwise, you need to specify the relative or absolute path of the file as well.
f = open("../my_data/example.txt")  # relative path
f.close()
f = open("/home/my_user/Coursera-Python-3-Programming/Python-Functions-Files-and-Dictionaries/my_data.txt",
         "r")  # absolute path
f.close()
# Absolute paths are not recommended. Relative paths are preferred because you won’t need to change your code when
# moving your project, if you preserve its internal structure.

# Note that python pathnames follow the UNIX conventions (Mac OS is a UNIX variant), rather than the Windows file
# pathnames that use : and ‘’. The python interpreter will translate to Windows pathnames when running on a Windows
# machine; you should be able to share your python program between a Windows machine and a MAC without having to rewrite
# the file open commands.
